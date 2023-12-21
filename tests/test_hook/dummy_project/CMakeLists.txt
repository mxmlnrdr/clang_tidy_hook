cmake_minimum_required(VERSION 3.16)

project(DummyProject)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_STANDARD 14)

set(SOURCE_FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/err.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ok.cpp)

add_library(DummyProject STATIC ${SOURCE_FILES})

target_include_directories(
  DummyProject
  PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>/include)
