 # Copyright 2017 Patrick Pedersen <ctx.xda@gmail.com>
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.

# Simple user I/O script that introduces someone

# Get some data about the user
age = input("Enter your age: ")   # Get age from user (age will be returned as str)
name = input("Enter your name: ") # Get name fro user

# Introduce
print("Let me introduce you to " + name + " he's " + age + " years old")

age = int(age) # Convert to int

print("He'd be", age * 2, "years old if he was twice as old as now")
