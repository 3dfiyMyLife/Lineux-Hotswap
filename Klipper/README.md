# Overview
Bikin Toolchanger (BTC) is using pure macros. It uses snippets of codes from the [Magswitch](https://github.com/jera-sea/MagSwitch-Toolchanger) project and the
[Klicky Probe](https://github.com/jlas1/Klicky-Probe).

# Nozzle Offset Calibration Tool
You can use Tubby, Intai, Nudge, Mellow Zero Precision, or any camera calibration or manual calibration. 

# Macro Status
Fully tested and working. Released.

# Instructions
Instructions are [here](https://github.com/3dfiyMyLife/Lineux-Toolchanger/blob/main/Manual/KLIPPER.md)

# Files
1. btc.cfg <- Main file, required
2. btc_carriage.cfg	<- Carriage file, required
3. btc_variables.cfg <- Variables, required
4. tool_x.cfg <- Individual tool settings, required
5. btc_leds.cfg <- Leds macros, required
6. dockslide.cfg <- Required if using dockslide
7. bashed_macros.cfg <- For stress testing of hotendchanger, required after set up
8. btc_tubby.cfg <- Macros for tubby tool, required during nozzle offset calibration set up
9. btc_tubby_z.cfg <- Macros for Z calibration only if using camera for X and Y nozzle offset
10. btc_extras.cfg <- Sample macros to use in start/end print and homing override
11. btc_spoolman.cfg <- Required if using Spoolman

# Video guide

[![IMAGE ALT TEXT HERE](https://github.com/3dfiyMyLife/Lineux-Hotswap/blob/main/Images/btc_klipper_hotswap.png)](https://youtu.be/aBgHKiLgzWA?si=D5ylQy5s1Cmdv41K)

