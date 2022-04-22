# Interstellar Intcode Program
# You're the captain, pilot, and engineer of the USS Supernova (a flying saucer). Your mission: to search the galaxy for a rare extraterrestrial creature known as the Space Pig 🐷🚀. Suddenly, your ship computer starts beeping. Uh oh... what's going on here? Thankfully, the Supernova's AI assistant is already explaining what's going on: "Don't worry," she says in a cheerful voice, "this is totally norma—"

# The Supernova's computer bursts into flames!!!!!!

# The computer was responsible for running Intcode programs that are essential for your safe passage across the stars. Needless to say you MUST rebuild the Intcode computer!!!

# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). 
# Here, you will find an opcode — either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.
def coding_challenge(integer_list):
    for i in range(0, len(integer_list),4):
        if integer_list[i] == 99:
            break
        elif integer_list[i] == 1:
            first_sum_index = integer_list[integer_list[i+1]]
            second_sum_index = integer_list[integer_list[i+2]]
            new_sum_value = first_sum_index + second_sum_index
            integer_list[integer_list[i+3]] = new_sum_value
        elif integer_list[i] == 2:
            first_multiplicand_index = integer_list[i+1]
            second_multiplicand_index = integer_list[i+2]
            new_product = integer_list[first_multiplicand_index] * integer_list[second_multiplicand_index]
            integer_list[integer_list[i+3]] = new_product
    return integer_list

print(coding_challenge([1,9,10,3,2,3,11,0,99,30,40,50]))
print(coding_challenge([1,0,0,0,99]))
print(coding_challenge([1,1,1,4,99,5,6,0,99]))
   
gravity_assist_program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0]
print(coding_challenge(gravity_assist_program))   
        
        
# Opcode 1 adds together numbers read from two positions and stores the result in a third position. 
# The three integers immediately after the opcode tell you these three positions — 
# the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

# For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

# Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

# For example, suppose you have the following program:

# 1,9,10,3,2,3,11,0,99,30,40,50
# For the purposes of illustration, here is the same program split into multiple lines:

# 1,9,10,3,
# 2,3,11,0,
# 99,
# 30,40,50
# The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together, they represent the first opcode (1, addition), the positions of the two inputs (9 and 10), and the position of the output (3). To handle this opcode, you first need to get the values at the input positions: position 9 contains 30, and position 10 contains 40. Add these numbers together to get 70. Then, store this value at the output position; here, the output position (3) is at position 3, so it overwrites itself. Afterward, the program looks like this:

# 1,9,10,70,
# 2,3,11,0,
# 99,
# 30,40,50
# Step forward 4 positions to reach the next opcode, 2. This opcode works just like the previous, but it multiplies instead of adding. The inputs are at positions 3 and 11; these positions contain 70 and 50 respectively. Multiplying these produces 3500; this is stored at position 0:

# 3500,9,10,70,
# 2,3,11,0,
# 99,
# 30,40,50
# Stepping forward 4 more positions arrives at opcode 99, halting the program.

# Here are the initial and final states of a few more small programs:

# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
# Once you have a working computer, the first step is to execute the gravity assist program:

# Gravity assist intcode program
# 1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0
# Before you run it though, you need to first restore it to the state it had just before the computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

# 🤫 PSST! Here's the answer (use this to test your code)