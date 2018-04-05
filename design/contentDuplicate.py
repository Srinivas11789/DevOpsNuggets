import os 
import hashlib

def contentDuplicates(dir):
        
        # File content dictionary data structure to make a decision on the duplicates
        filecontent = {}

	for dir, subdir, filenames in os.walk(dir):
            
            # Debug print - all the filenames
	    #print filenames
         
            for filename in filenames:
                
		# Debug - filenames with absolute path rather than relative path
		#print os.path.abspath(filename) or print os.path.join(dir+'/'+filename)
                
		"""
                ######### 1st thoughts
                # Naive logic of storing all the content as a key in the dictionary and filenames as list of duplicates 
		# Cons: Full content replica as a key -- memory hogging or exhaust - try to optimize
		
                content = open(os.path.join(dir+'/'+filename), 'r').read()
                if content not in filecontent:
                           filecontent[content] = []
                filecontent[content].append(os.path.abspath(filename))
		"""
     		
		######### Thoughts...
 		# Optimizing the memory as larger content may crash the program or exhaust the memory.
                # Thinking....
                # Vaibhav discussion and input
                # * Storing only part of the content and narrowing the duplicates, further iterating this activity to find full duplicates
                # * Storing it on a nosql db or any db and retrieve?
                # * A very nice thought from **** - why not use hashfunctions
		"""
                ######### 2nd
                # Pros: Memory problem solved 
                # Cons: stress on the CPU for computing the hash everytime
                content = hashlib.md5(open(os.path.join(dir+'/'+filename), 'r').read()).hexdigest()
                if content not in filecontent:
                           filecontent[content] = []
                filecontent[content].append(os.path.abspath(filename))
		"""
                ########## Thoughts...
                # Optimize CPU utilization
                # Thinking....
		# * reduced and simpler hash function like just xor
                # ** TradeOff: possibility of easy collision occurence or occurence of false duplicates
              	# ** Solution to Tradeoff:
                #    ** Initially using les complex hash function or simple xor, further narrowing down with hash function for a strict output
			
		########## 3rd
                # simple xor to reduce cpu stress
                # Cons: reading the file again for calculating the hash

                key = ord('x')
		content = open(os.path.join(dir+'/'+filename), 'r').read()
                content = "".join([chr(ord(c1) ^ key) for c1 in content])
                if content not in filecontent:
                           filecontent[content] = []
                filecontent[content].append(os.path.abspath(filename))
	
        # Strict check for possibility of false duplicates
        # If false duplicate occurs, delete the xor key and replace it with hash key
        for key,value in filecontent.items():
                    print value
                    if len(value) > 1:
                       check = []
                       for v in value:
                       		content = hashlib.md5(open(os.path.join(dir+'/'+filename), 'r').read()).hexdigest()
                       		if content not in filecontent:
                        	   filecontent[content] = []
                       		filecontent[content].append(os.path.abspath(filename))
                    if len(value) != len(filecontent[content]):
                                print "False duplicated occurred!"
                                del filecontent[key]


		############# 4th 
                # Possibility of a disk usage reduction 
                ### Thinking...
                # Discussion with Vaibhav - every file should be visited atleast once - how to not visit it to hash again?
                # Reduced disk operations???

	# Debug result
        print filecontent
            

def main():
    dir = "/Users/darkknight/Desktop/Github_Repo/algos/devOpsNuggets/design/test"
    contentDuplicates(dir)

main()
