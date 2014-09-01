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
include examples/libplayerc++/CMakeFiles/example2.dir/depend.make

# Include the progress variables for this target.
include examples/libplayerc++/CMakeFiles/example2.dir/progress.make

# Include the compile flags for this target's objects.
include examples/libplayerc++/CMakeFiles/example2.dir/flags.make

examples/libplayerc++/CMakeFiles/example2.dir/example2.o: examples/libplayerc++/CMakeFiles/example2.dir/flags.make
examples/libplayerc++/CMakeFiles/example2.dir/example2.o: ../examples/libplayerc++/example2.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/local/src/player-3.0.2/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object examples/libplayerc++/CMakeFiles/example2.dir/example2.o"
	cd /usr/local/src/player-3.0.2/build/examples/libplayerc++ && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/example2.dir/example2.o -c /usr/local/src/player-3.0.2/examples/libplayerc++/example2.cc

examples/libplayerc++/CMakeFiles/example2.dir/example2.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example2.dir/example2.i"
	cd /usr/local/src/player-3.0.2/build/examples/libplayerc++ && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /usr/local/src/player-3.0.2/examples/libplayerc++/example2.cc > CMakeFiles/example2.dir/example2.i

examples/libplayerc++/CMakeFiles/example2.dir/example2.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example2.dir/example2.s"
	cd /usr/local/src/player-3.0.2/build/examples/libplayerc++ && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /usr/local/src/player-3.0.2/examples/libplayerc++/example2.cc -o CMakeFiles/example2.dir/example2.s

examples/libplayerc++/CMakeFiles/example2.dir/example2.o.requires:
.PHONY : examples/libplayerc++/CMakeFiles/example2.dir/example2.o.requires

examples/libplayerc++/CMakeFiles/example2.dir/example2.o.provides: examples/libplayerc++/CMakeFiles/example2.dir/example2.o.requires
	$(MAKE) -f examples/libplayerc++/CMakeFiles/example2.dir/build.make examples/libplayerc++/CMakeFiles/example2.dir/example2.o.provides.build
.PHONY : examples/libplayerc++/CMakeFiles/example2.dir/example2.o.provides

examples/libplayerc++/CMakeFiles/example2.dir/example2.o.provides.build: examples/libplayerc++/CMakeFiles/example2.dir/example2.o

# Object files for target example2
example2_OBJECTS = \
"CMakeFiles/example2.dir/example2.o"

# External object files for target example2
example2_EXTERNAL_OBJECTS =

examples/libplayerc++/example2: examples/libplayerc++/CMakeFiles/example2.dir/example2.o
examples/libplayerc++/example2: client_libs/libplayerc++/libplayerc++.so.3.0.2
examples/libplayerc++/example2: client_libs/libplayerc/libplayerc.so.3.0.2
examples/libplayerc++/example2: libplayerinterface/libplayerinterface.so.3.0.2
examples/libplayerc++/example2: libplayercommon/libplayercommon.so.3.0.2
examples/libplayerc++/example2: libplayerjpeg/libplayerjpeg.so.3.0.2
examples/libplayerc++/example2: libplayerwkb/libplayerwkb.so.3.0.2
examples/libplayerc++/example2: libplayercommon/libplayercommon.so.3.0.2
examples/libplayerc++/example2: examples/libplayerc++/CMakeFiles/example2.dir/build.make
examples/libplayerc++/example2: examples/libplayerc++/CMakeFiles/example2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable example2"
	cd /usr/local/src/player-3.0.2/build/examples/libplayerc++ && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/libplayerc++/CMakeFiles/example2.dir/build: examples/libplayerc++/example2
.PHONY : examples/libplayerc++/CMakeFiles/example2.dir/build

examples/libplayerc++/CMakeFiles/example2.dir/requires: examples/libplayerc++/CMakeFiles/example2.dir/example2.o.requires
.PHONY : examples/libplayerc++/CMakeFiles/example2.dir/requires

examples/libplayerc++/CMakeFiles/example2.dir/clean:
	cd /usr/local/src/player-3.0.2/build/examples/libplayerc++ && $(CMAKE_COMMAND) -P CMakeFiles/example2.dir/cmake_clean.cmake
.PHONY : examples/libplayerc++/CMakeFiles/example2.dir/clean

examples/libplayerc++/CMakeFiles/example2.dir/depend:
	cd /usr/local/src/player-3.0.2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/local/src/player-3.0.2 /usr/local/src/player-3.0.2/examples/libplayerc++ /usr/local/src/player-3.0.2/build /usr/local/src/player-3.0.2/build/examples/libplayerc++ /usr/local/src/player-3.0.2/build/examples/libplayerc++/CMakeFiles/example2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/libplayerc++/CMakeFiles/example2.dir/depend

