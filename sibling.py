set_A={"A","B","C","D","E"}
set_B={"B","D","V","X","Y","U"} #set union is a combination of two sets

union=set_A.union(set_B)
print(union)  #sets are only meant to have unique values so anything repeating would be picked only once

#intersection is what is in both sets
inter=set_A.intersection(set_B)
print(inter)  #basically picks elements that appear more than once in both sets

#additon rule states that = P(A_or_B)= P(A) + P(B) - P(intersection)
A={2,4,6}  #even numbers in a six sided dice
B={3,4,5,6}  #numbers greater than two in a six sided dice

prob_A=len(A)/6
prob_B=len(B)/6

inters=A.intersection(B)
prob_inters=len(inter)/6

prob_A_or_B=prob_A+prob_B-prob_inters #addition rule
print(prob_A_or_B)