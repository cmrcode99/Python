def reverse_characters(a_string):
 a_string_type= type(a_string) 
 if a_string_type != str:
   a_string= str(a_string)
 a_list= list(a_string)
 reversed_string= ''.join(reversed(a_list))
 reversed_string= a_string_type(reversed_string)
 return reversed_string
 
def list_reverse(a_list):
  new_list=[]
  for turn in range(len(a_list)):
    what_im_indexing=a_list[turn]
    reversed_string= reverse_characters(what_im_indexing)
    new_list.append(reversed_string)
  new_list.reverse()
  return new_list
  
test=['hello', 'world', 12.3, 'orange', 987,'apple', 'potato', 'Capitalized Words', 89.5, 12.35556]
print(list_reverse(test))
