# Install script for directory: /usr/local/src/player-3.0.2/examples/libplayerc++

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

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/player/examples/libplayerc++" TYPE FILE FILES
    "/usr/local/src/player-3.0.2/examples/libplayerc++/args.h"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/camera.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/example0.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/example4.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/grip.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/clientgraphics.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/clientgraphics3d.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/laserobstacleavoid.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/ptz.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/randomwalk.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/sonarobstacleavoid.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/speech.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/wallfollow.cc"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/player/examples/libplayerc++" TYPE FILE FILES
    "/usr/local/src/player-3.0.2/examples/libplayerc++/example1.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/example3.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/goto.cc"
    "/usr/local/src/player-3.0.2/examples/libplayerc++/speech_cpp_client.cc"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/player/examples/libplayerc++" TYPE FILE FILES "/usr/local/src/player-3.0.2/examples/libplayerc++/example2.cc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/player/examples/libplayerc++" TYPE FILE RENAME "CMakeLists.txt" FILES "/usr/local/src/player-3.0.2/build/examples/libplayerc++/CMakeLists.txt.example")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/player/examples/libplayerc++" TYPE FILE FILES "/usr/local/src/player-3.0.2/examples/libplayerc++/README")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "examples")

