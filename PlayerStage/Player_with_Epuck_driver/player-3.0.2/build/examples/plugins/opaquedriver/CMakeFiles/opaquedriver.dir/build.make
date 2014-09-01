# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /usr/local/src/player-3.0.2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr/local/src/player-3.0.2/build

# Include any dependencies generated for this target.
include examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/depend.make

# Include the progress variables for this target.
include examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/progress.make

# Include the compile flags for this target's objects.
include examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/flags.make

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/flags.make
examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o: ../examples/plugins/opaquedriver/opaquedriver.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/local/src/player-3.0.2/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o"
	cd /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/opaquedriver.dir/opaquedriver.o -c /usr/local/src/player-3.0.2/examples/plugins/opaquedriver/opaquedriver.cc

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opaquedriver.dir/opaquedriver.i"
	cd /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /usr/local/src/player-3.0.2/examples/plugins/opaquedriver/opaquedriver.cc > CMakeFiles/opaquedriver.dir/opaquedriver.i

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opaquedriver.dir/opaquedriver.s"
	cd /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /usr/local/src/player-3.0.2/examples/plugins/opaquedriver/opaquedriver.cc -o CMakeFiles/opaquedriver.dir/opaquedriver.s

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.requires:
.PHONY : examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.requires

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.provides: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.requires
	$(MAKE) -f examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/build.make examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.provides.build
.PHONY : examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.provides

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.provides.build: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o

# Object files for target opaquedriver
opaquedriver_OBJECTS = \
"CMakeFiles/opaquedriver.dir/opaquedriver.o"

# External object files for target opaquedriver
opaquedriver_EXTERNAL_OBJECTS =

examples/plugins/opaquedriver/libopaquedriver.so: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o
examples/plugins/opaquedriver/libopaquedriver.so: libplayercore/libplayercore.so.3.0.2
examples/plugins/opaquedriver/libopaquedriver.so: libplayerinterface/libplayerinterface.so.3.0.2
examples/plugins/opaquedriver/libopaquedriver.so: libplayercommon/libplayercommon.so.3.0.2
examples/plugins/opaquedriver/libopaquedriver.so: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/build.make
examples/plugins/opaquedriver/libopaquedriver.so: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared library libopaquedriver.so"
	cd /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/opaquedriver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/build: examples/plugins/opaquedriver/libopaquedriver.so
.PHONY : examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/build

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/requires: examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/opaquedriver.o.requires
.PHONY : examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/requires

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/clean:
	cd /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver && $(CMAKE_COMMAND) -P CMakeFiles/opaquedriver.dir/cmake_clean.cmake
.PHONY : examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/clean

examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/depend:
	cd /usr/local/src/player-3.0.2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/local/src/player-3.0.2 /usr/local/src/player-3.0.2/examples/plugins/opaquedriver /usr/local/src/player-3.0.2/build /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver /usr/local/src/player-3.0.2/build/examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/plugins/opaquedriver/CMakeFiles/opaquedriver.dir/depend

