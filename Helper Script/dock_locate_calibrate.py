# Nozzle alignment / dock location calibration module
#
# Lineux Hotswap Dock Location Calibration
#
# Adapted from code originally used by:
# Klipper_ToolChanger / probe_multi_axis.py
#
# The calibration determines the dock location by comparing
# CoreXY stepper MCU positions before and after the calibration
# movement.
#
# Dock location calculation:
#
#   X = X endstop + calculated X offset
#   Y = Y endstop + calculated Y offset
#
# The calibration movement itself is NOT subtracted from the
# final dock coordinates.


import logging


class DockLocateCalibrate:

    def __init__(self, config):

        self.printer = config.get_printer()
        self.name = config.get_name()

        # ----------------------------------------------------
        # Configuration
        # ----------------------------------------------------

        # MCU position resolution in mm per MCU step.
        self.xy_resolution = config.getfloat('xy_resolution')

        # Actual printer homing/endstop positions.
        #
        # These should match:
        #
        # [stepper_x]
        # position_endstop:
        #
        # [stepper_y]
        # position_endstop:
        #
        # They are NOT bed dimensions or position_max.
        self.x_endstop = config.getfloat('x_endstop')
        self.y_endstop = config.getfloat('y_endstop')

        # Calibration movement distance.
        #
        # Positive value = move X positive
        # Negative value = move X negative
        self.calibrate_move_x = config.getfloat('calibrate_move_x')

        # ----------------------------------------------------
        # Klipper objects
        # ----------------------------------------------------

        self.gcode = self.printer.lookup_object('gcode')

        # ----------------------------------------------------
        # Register G-Code command
        # ----------------------------------------------------

        self.gcode.register_command(
            'DOCK_LOCATE_CALIBRATE',
            self.cmd_DOCK_LOCATE_CALIBRATE,
            desc=self.cmd_DOCK_LOCATE_CALIBRATE_help
        )

    # --------------------------------------------------------
    # Status
    # --------------------------------------------------------

    def get_status(self, eventtime):
        return {}

    # --------------------------------------------------------
    # Get MCU stepper positions
    # --------------------------------------------------------

    def get_mcu_position(self):

        toolhead = self.printer.lookup_object('toolhead')
        steppers = toolhead.kin.get_steppers()

        mcu_pos_x = None
        mcu_pos_y = None

        for stepper in steppers:

            name = stepper.get_name()

            if name == "stepper_x":
                mcu_pos_x = stepper.get_mcu_position()

            elif name == "stepper_y":
                mcu_pos_y = stepper.get_mcu_position()

        if mcu_pos_x is None or mcu_pos_y is None:
            raise self.printer.command_error(
                "Unable to obtain X/Y MCU stepper positions"
            )

        return {
            'x': mcu_pos_x,
            'y': mcu_pos_y
        }

    # --------------------------------------------------------
    # Calibration command
    # --------------------------------------------------------

    cmd_DOCK_LOCATE_CALIBRATE_help = (
        "Calculate Lineux Hotswap dock location"
    )

    def cmd_DOCK_LOCATE_CALIBRATE(self, gcmd):

        # ----------------------------------------------------
        # Record initial MCU position
        # ----------------------------------------------------

        initial_res = self.get_mcu_position()

        logging.info(
            "Lineux Dock Calibration - "
            "Initial MCU position: X=%s Y=%s",
            initial_res['x'],
            initial_res['y']
        )

        # ----------------------------------------------------
        # Establish temporary kinematic position
        # ----------------------------------------------------

        self.gcode.run_script_from_command(
            'SET_KINEMATIC_POSITION'
        )

        # ----------------------------------------------------
        # Perform calibration movement
        #
        # The direction and distance are controlled by:
        #
        #   calibrate_move_x
        #
        # Example:
        #
        #   3.0  -> G1 X3
        #  -3.0  -> G1 X-3
        # ----------------------------------------------------

        self.gcode.run_script_from_command(
            'G91'
        )

        self.gcode.run_script_from_command(
            'G1 X%.3f F3000' % self.calibrate_move_x
        )

        self.gcode.run_script_from_command(
            'G90'
        )

        # ----------------------------------------------------
        # Home Y
        # ----------------------------------------------------

        self.gcode.run_script_from_command(
            'G28 Y'
        )

        # ----------------------------------------------------
        # Wait 1 second
        # ----------------------------------------------------

        self.gcode.run_script_from_command(
            'G4 P1000'
        )

        # ----------------------------------------------------
        # Home X
        # ----------------------------------------------------

        self.gcode.run_script_from_command(
            'G28 X'
        )

        # ----------------------------------------------------
        # Record final MCU position
        # ----------------------------------------------------

        final_res = self.get_mcu_position()

        logging.info(
            "Lineux Dock Calibration - "
            "Final MCU position: X=%s Y=%s",
            final_res['x'],
            final_res['y']
        )

        # ----------------------------------------------------
        # Calculate MCU movement
        # ----------------------------------------------------

        dx = final_res['x'] - initial_res['x']
        dy = final_res['y'] - initial_res['y']

        # ----------------------------------------------------
        # Calculate raw dock offsets
        #
        # CoreXY relationship:
        #
        #   X = -(dx + dy) / 2
        #   Y = -(dx - dy) / 2
        #
        # Then convert MCU steps to millimeters.
        # ----------------------------------------------------

        raw_dock_x = (
            -((dx + dy) / 2.0)
            * self.xy_resolution
        )

        raw_dock_y = (
            -((dx - dy) / 2.0)
            * self.xy_resolution
        )

        # ----------------------------------------------------
        # Calculate actual dock coordinates
        #
        # IMPORTANT:
        #
        # The calibration movement is NOT subtracted here.
        # ----------------------------------------------------

        dock_x = self.x_endstop + raw_dock_x
        dock_y = self.y_endstop + raw_dock_y

        # ----------------------------------------------------
        # Report results
        # ----------------------------------------------------

        gcmd.respond_info(
            "Lineux Hotswap Dock Calibration\n"
            "--------------------------------\n"
            "Initial MCU: X=%s Y=%s\n"
            "Final MCU:   X=%s Y=%s\n"
            "MCU Delta:   X=%s Y=%s\n"
            "XY Resolution: %.7f mm/step\n"
            "X Endstop: %.2f mm\n"
            "Y Endstop: %.2f mm\n"
            "Calibration Move: %.2f mm\n"
            "Raw Offset: X=%.2f Y=%.2f mm\n"
            "Calculated Dock Location:\n"
            "X: %.2f mm\n"
            "Y: %.2f mm"
            % (
                initial_res['x'],
                initial_res['y'],
                final_res['x'],
                final_res['y'],
                dx,
                dy,
                self.xy_resolution,
                self.x_endstop,
                self.y_endstop,
                self.calibrate_move_x,
                raw_dock_x,
                raw_dock_y,
                dock_x,
                dock_y
            )
        )


# ------------------------------------------------------------
# Klipper module loader
# ------------------------------------------------------------

def load_config(config):
    return DockLocateCalibrate(config)