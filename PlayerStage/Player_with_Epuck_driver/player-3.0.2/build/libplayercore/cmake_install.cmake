# Install script for directory: /usr/local/src/player-3.0.2/libplayercore

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

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "libraries")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64" TYPE SHARED_LIBRARY FILES
    "/usr/local/src/player-3.0.2/build/libplayercore/libplayercore.so.3.0.2"
    "/usr/local/src/player-3.0.2/build/libplayercore/libplayercore.so.3.0"
    "/usr/local/src/player-3.0.2/build/libplayercore/libplayercore.so"
    )
  FOREACH(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/libplayercore.so.3.0.2"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/libplayercore.so.3.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/libplayercore.so"
      )
    IF(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      IF(CMAKE_INSTALL_DO_STRIP)
        EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "${file}")
      ENDIF(CMAKE_INSTALL_DO_STRIP)
    ENDIF()
  ENDFOREACH()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "libraries")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "pkgconfig")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/pkgconfig" TYPE FILE FILES "/usr/local/src/player-3.0.2/build/libplayercore/playercore.pc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "pkgconfig")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "headers")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/player-3.0/libplayercore" TYPE FILE FILES
    "/usr/local/src/player-3.0.2/libplayercore/configfile.h"
    "/usr/local/src/player-3.0.2/libplayercore/device.h"
    "/usr/local/src/player-3.0.2/libplayercore/devicetable.h"
    "/usr/local/src/player-3.0.2/libplayercore/driver.h"
    "/usr/local/src/player-3.0.2/libplayercore/drivertable.h"
    "/usr/local/src/player-3.0.2/libplayercore/filewatcher.h"
    "/usr/local/src/player-3.0.2/libplayercore/globals.h"
    "/usr/local/src/player-3.0.2/libplayercore/message.h"
    "/usr/local/src/player-3.0.2/libplayercore/playercore.h"
    "/usr/local/src/player-3.0.2/libplayercore/playertime.h"
    "/usr/local/src/player-3.0.2/libplayercore/plugins.h"
    "/usr/local/src/player-3.0.2/libplayercore/property.h"
    "/usr/local/src/player-3.0.2/libplayercore/wallclocktime.h"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "headers")

