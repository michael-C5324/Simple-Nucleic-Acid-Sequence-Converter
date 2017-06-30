#This script will take a DNA, mRNA, or tRNA strand sequence and return the other corresponding strands.
#At present it is necessary to copy and past outputs for use in other programs but I may add on more functionality at some point.
#-------------------------------------------------------------------------------------------------------------------------------

import os

###Dictionaries for converting between different nucleic acid types###
###There might be a better way to do this but it works for now lol###
DNA_dic = {"A" : "T", "C" : "G", "T" : "A", "G" : "C",
           "a" : "T", "c" : "G", "t" : "A", "g" : "C"}

DNA_to_mRNA = {"A" : "U", "C" : "G", "T" : "A", "G" : "C",
               "a" : "U", "c" : "G", "t" : "A", "g" : "C"}
               
mRNA_to_tRNA = {"A" : "U", "C" : "G", "U" : "A", "G" : "C",
               "a" : "U", "c" : "G", "u" : "A", "g" : "C"}
               
mRNA_to_DNA = {"A" : "T", "C" : "G", "U" : "A", "G" : "C",
               "a" : "T", "c" : "G", "u" : "A", "g" : "C"}

tRNA_to_mRNA = {"A" : "U", "C" : "G", "U" : "A", "G" : "C",
               "a" : "U", "c" : "G", "u" : "A", "g" : "C"}


###Boring Title Sequence but atleast its centered###
width = os.get_terminal_size().columns
print("=".center(width,"="))
print(" Nucleic Acid Sequence Converter ".center(width, "="))
print("=".center(width,"="))
print(" ")

              
while True:
    init = input("Is it a DNA or RNA Sequence? ")

###Defines the user input as a DNA strand and converts the strand to complementary DNA, mRNA, and tRNA strand###
    if "D" in init or "d" in init:
        DNA_input = list(input("Input primary DNA Strand Sequence "))
        Complementary_DNA_Strand = [DNA_dic[n] for n in DNA_input]
        mRNA_Strand = [DNA_to_mRNA[n] for n in DNA_input]
        tRNA_Strand = [mRNA_to_tRNA[n] for n in mRNA_Strand]
       
###Block converting list values back to strings before printing###
        print(" ")
        print("Input Primary Strand:")
        print(''.join(DNA_input))
        print(" ")
        print("Complementary DNA Strand:")
        print(''.join(Complementary_DNA_Strand))
        print(" ")
        print("Corresponding mRNA Strand:")
        print(''.join(mRNA_Strand))
        print(" ")
        print("Corresponding tRNA Strand:")
        print(''.join(tRNA_Strand))
        print(" ")
        print("-".center(width, "-"))
    
###Defines the user input as a type of RNA strand### 
    if "R" in init or "r" in init:
        question = input("Is this an mRNA or tRNA strand? ")
        
###Defines the type of RNA as mRNA and converts the strand to DNA and tRNA strands###
        if "M" in question or "m" in question:
            mRNA_Input = list(input("Input mRNA Strand Sequence "))
            DNA_Strand = [mRNA_to_DNA[n] for n in mRNA_Input]
            tRNA_Strand = [mRNA_to_tRNA[n] for n in mRNA_Input]

###Block converting list values back to strings before printing###            
            print(" ")
            print("Input mRNA Strand:")
            print(''.join(mRNA_Input))
            print(" ")
            print("Initial DNA Strand: ")
            print(''.join(DNA_Strand))
            print(" ")
            print("Corresponding tRNA Strand: ")
            print(''.join(tRNA_Strand))
            print(" ")
            print("-".center(width, "-"))

###Defines the type of RNA as tRNA and converts the strand back to mRNA and initial DNA strands###            
        elif "T" in question or "t" in question:
           tRNA_Input = list(input("Input tRNA Strand Sequence "))
           mRNA_Strand = [tRNA_to_mRNA[n] for n in tRNA_Input]
           DNA_Strand = [mRNA_to_DNA[n] for n in mRNA_Strand]

###Block converting list values back to strings before printing###                       
           print(" ")
           print("Input tRNA Strand:")
           print(''.join(tRNA_Input))
           print(" ")
           print("Corresponding mRNA Strand: ")
           print(''.join(mRNA_Strand))
           print(" ")
           print("Initial DNA Strand: ")
           print(''.join(DNA_Strand))
           print(" ")
           print("-".center(width, "-"))

