SUBDIRS = src doc/doxygen

EXTRA_DIST = ./Doxyfile \
             ./doc/camera_config.dox \
             ./doc/examples.dox \
             ./doc/main_page.dox \
             ./doc/player2_0.dox \
             ./doc/player2_1.dox

if PLAYER_2_0
examplesdir = $(docdir)/examples/
dist_examples_DATA = ./doc/player_2_0/epuck.cfg \
                     ./doc/player_2_0/position2d.c \
                     ./doc/player_2_0/ir.c \
                     ./doc/player_2_0/camera.c \
                     ./doc/player_2_0/Makefile \
                     ./doc/player_2_0/opaqueLED.c
endif

if PLAYER_2_1
examplesdir = $(docdir)/examples/
dist_examples_DATA = ./doc/player_2_1/blinkenlight.c \
                     ./doc/player_2_1/epuck.cfg \
                     ./doc/player_2_1/Makefile \
                     ./doc/player_2_1/camera.c \
                     ./doc/player_2_1/ir.c \
                     ./doc/player_2_1/position2d.c
endif

epucksidedir = $(datadir)/libEpuckPlayer/epuckSide
dist_epuckside_DATA = ./epuckSide/epuckPlayer.c \
                      ./epuckSide/linker.py \
                      ./epuckSide/main.c \
                      ./epuckSide/Makefile \
                      ./epuckSide/README \
                      ./epuckSide/outputV300.hex

libObjdir = $(datadir)/libEpuckPlayer/epuckSide/libObj
dist_libObj_DATA = ./epuckSide/libObj/e_ad_conv.o \
                   ./epuckSide/libObj/e_agenda.o \
                   ./epuckSide/libObj/e_calc_po3030k.o \
                   ./epuckSide/libObj/e_calc_po6030k.o \
                   ./epuckSide/libObj/e_common.o \
                   ./epuckSide/libObj/e_I2C_master_module.o \
                   ./epuckSide/libObj/e_I2C_protocol.o \
                   ./epuckSide/libObj/e_init_port.o \
                   ./epuckSide/libObj/e_init_uart1.o \
                   ./epuckSide/libObj/e_interrupt.o \
                   ./epuckSide/libObj/e_led.o \
                   ./epuckSide/libObj/e_motors.o \
                   ./epuckSide/libObj/e_prox.o \
                   ./epuckSide/libObj/e_po3030k_registers.o \
                   ./epuckSide/libObj/e_po6030k_registers.o \
                   ./epuckSide/libObj/e_timers.o \
                   ./epuckSide/libObj/e_uart1_rx_char.o \
                   ./epuckSide/libObj/e_uart1_tx_char.o
