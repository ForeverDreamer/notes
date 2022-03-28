cmake_minimum_required(VERSION 3.16)
project(test)

set(CMAKE_CXX_STANDARD 14)

add_executable(test main.cpp)
add_library(test_library STATIC src/Functions.cpp)
find_library(TEST_LIBRARY test_library lib)
target_link_libraries(test LINK_PUBLIC ${TEST_LIBRARY})
