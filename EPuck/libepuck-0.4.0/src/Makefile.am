lib_LTLIBRARIES = libepuck.la
libepuck_la_CPPFLAGS = -Wall

libepuck_la_SOURCES = serialPort.hpp \
                      serialPort.cpp \
                      timer.hpp \
                      epuckInterface.hpp \
                      epuckInterface.cpp \
                      epuckPosition2d.hpp \
                      epuckPosition2d.cpp \
                      epuckIR.hpp \
                      epuckIR.cpp \
                      epuckCamera.hpp \
                      epuckCamera.cpp \
                      epuckLEDs.hpp \
                      epuckLEDs.cpp

if PLAYER_2_0
libepuck_la_CPPFLAGS += $(PLAYERCORE_2_0_CFLAGS)
libepuck_la_SOURCES += epuckDriver2_0.hpp \
                       epuckDriver2_0.cpp
endif

if PLAYER_2_1
libepuck_la_CPPFLAGS += $(PLAYERCORE_2_1_CFLAGS)
libepuck_la_SOURCES += epuckDriver2_1.hpp \
                       epuckDriver2_1.cpp
endif


#libepuck_la_LDFLAGS = $(PLAYERCORE_LIBS) -version-info 0:0:0
libepuck_la_LDFLAGS = -version-info 0:4:0
