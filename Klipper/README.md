# Overview
Bikin Toolchanger (BTC) is using pure macros. It uses snippets of codes from the [Magswitch](https://github.com/jera-sea/MagSwitch-Toolchanger) project and the
[Klicky Probe](https://github.com/jlas1/Klicky-Probe).

# Nozzle Offset Calibration Tool
You can use Tubby, Intai, Mellow Zero Precision, or any camera calibration or manual calibration. 

# Macro Status
Fully tested and working. Released. (to be consolidated)

# Instructions
Instructions are [here](https://github.com/Bikin-Creative/Lineux-Toolchanger/blob/main/Manual/KLIPPER.md)

# Files
1. btc.cfg <- Main file, required
2. btc_variables.cfg <- Variables, required
3. tool_x.cfg <- Individual tool settings, required
4. btc_leds.cfg <- Leds macros, required
5. dockslide.cfg <- Required if using dockslide
6. bashed_macros.cfg <- For stress testing of toolchanger, required after set up
7. btc_nudge.cfg <- Macros for nudge tool, required during nozzle offset calibration set up
8. btc_tubby_z.cfg <- Macros for Z calibration only if using camera for X and Y nozzle offset
9. btc_extras <- Sample macros to use in start/end print and homing override
10. btc_spoolman.cfg <- Currently not in used

# Video guide

[![IMAGE ALT TEXT HERE](https://github.com/Bikin-Creative/Lineux-Toolchanger/blob/main/Images/btc_guide.png)](https://youtu.be/QYzVRNqW2J0?si=Q4HBHzA9LW7UP1U8)

