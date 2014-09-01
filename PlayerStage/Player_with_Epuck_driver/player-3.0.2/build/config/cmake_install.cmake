# Install script for directory: /usr/local/src/player-3.0.2/config

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "samplecfg")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/player/config" TYPE FILE FILES
    "/usr/local/src/player-3.0.2/config/afsm.cfg"
    "/usr/local/src/player-3.0.2/config/afsm.eps"
    "/usr/local/src/player-3.0.2/config/amigobot.cfg"
    "/usr/local/src/player-3.0.2/config/amigobot_tcp.cfg"
    "/usr/local/src/player-3.0.2/config/amtecM5.cfg"
    "/usr/local/src/player-3.0.2/config/b21r_rflex_lms200.cfg"
    "/usr/local/src/player-3.0.2/config/cvcam.cfg"
    "/usr/local/src/player-3.0.2/config/dummy.cfg"
    "/usr/local/src/player-3.0.2/config/erratic.cfg"
    "/usr/local/src/player-3.0.2/config/hokuyo_aist.cfg"
    "/usr/local/src/player-3.0.2/config/iwspy.cfg"
    "/usr/local/src/player-3.0.2/config/joystick.cfg"
    "/usr/local/src/player-3.0.2/config/lms400.cfg"
    "/usr/local/src/player-3.0.2/config/magellan.cfg"
    "/usr/local/src/player-3.0.2/config/mapfile.cfg"
    "/usr/local/src/player-3.0.2/config/mbicp.cfg"
    "/usr/local/src/player-3.0.2/config/nomad.cfg"
    "/usr/local/src/player-3.0.2/config/obot.cfg"
    "/usr/local/src/player-3.0.2/config/passthrough.cfg"
    "/usr/local/src/player-3.0.2/config/phidgetIFK.cfg"
    "/usr/local/src/player-3.0.2/config/phidgetRFID.cfg"
    "/usr/local/src/player-3.0.2/config/pioneer.cfg"
    "/usr/local/src/player-3.0.2/config/pioneer_rs4euze.cfg"
    "/usr/local/src/player-3.0.2/config/pointcloud3d.cfg"
    "/usr/local/src/player-3.0.2/config/readlog.cfg"
    "/usr/local/src/player-3.0.2/config/rfid.cfg"
    "/usr/local/src/player-3.0.2/config/roomba.cfg"
    "/usr/local/src/player-3.0.2/config/searchpattern.cfg"
    "/usr/local/src/player-3.0.2/config/searchpattern_symbols.ps"
    "/usr/local/src/player-3.0.2/config/segwayrmp.cfg"
    "/usr/local/src/player-3.0.2/config/service_adv.cfg"
    "/usr/local/src/player-3.0.2/config/simple.cfg"
    "/usr/local/src/player-3.0.2/config/sphere.cfg"
    "/usr/local/src/player-3.0.2/config/umass_ATRVJr.cfg"
    "/usr/local/src/player-3.0.2/config/umass_ATRVMini.cfg"
    "/usr/local/src/player-3.0.2/config/umass_reb.cfg"
    "/usr/local/src/player-3.0.2/config/urglaser.cfg"
    "/usr/local/src/player-3.0.2/config/vfh.cfg"
    "/usr/local/src/player-3.0.2/config/wavefront.cfg"
    "/usr/local/src/player-3.0.2/config/wbr914.cfg"
    "/usr/local/src/player-3.0.2/config/writelog.cfg"
    "/usr/local/src/player-3.0.2/config/wsn.cfg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "samplecfg")

