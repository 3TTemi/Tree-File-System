class TreeNode: 

    # initialization of tree node
    def __init__(self, filename, children = None, parent = None):
        self.filename = filename 
        self.children = []
        self.parent = parent 
    
    # function to asssit in adding tree node
    def addChild(self, child):
        self.children.append(child) 
        child.parent = self  

    #Helper function to DFS that actually utilizes recursion
    def DFS(self, pos, path): 

        # choosing by adding current position to path
        path.append("/" + pos.filename)

        #base case if pdf is found
        if pos.filename[-4:] == ".pdf": 
            #joins the path list into string to print
            print("".join(path))

        #traversing through more children (exploring)  
        curlist = pos.children
        for cur in curlist:
            self.DFS(cur, path)

        path.pop()


    def BFS(self, pos):

        #entryPath is set to only include the root
        entryPath = [pos]
        #allLists act as queue to traverse each level at a time
        allLists = []
        allLists.append(entryPath)
        # iterates while the queue is not empty
        while len(allLists) > 0:

            # last element in path is stored to check whether its target and add children
            pathCur = allLists.pop()

            # if pdf is found in the last part of current path, path is created into string
            if pathCur[-1].filename[-4:] == ".pdf":
                str = ""
                for i in range(len(pathCur)):
                    str += "/" + pathCur[i].filename
                # return str
                print(str)

            #adds a list which all children to queue
            for child in pathCur[-1].children:
                pathCopy = pathCur.copy()
                pathCopy.append(child)
                allLists.append(pathCopy)
        


def main(): 

    # initalizing and creating the tree 
    rootNode = TreeNode("rootFolder") 
    important = TreeNode("important.pdf")
    rootNode.addChild(important)

    documents = TreeNode("documents")
    homework = TreeNode("homework")
    hw1 = TreeNode("hw1.pdf")
    hw2 = TreeNode("hw2.pdf")
    essay1 = TreeNode("essay1.pdf")
    essay2 = TreeNode("essay2.pdf")

    rootNode.addChild(documents)
    documents.addChild(homework)
    homework.addChild(hw1)
    homework.addChild(hw2)
    documents.addChild(essay1)
    documents.addChild(essay2)

    downloads = TreeNode("downloads")
    movie = TreeNode("movie.pdf")
    funStuff = TreeNode("funStuff")
    rootNode.addChild(downloads)
    downloads.addChild(movie)
    downloads.addChild(funStuff)

    desktop = TreeNode("desktop")
    items = TreeNode("items")
    schedule = TreeNode("schedule.pdf")
    
    rootNode.addChild(desktop)
    desktop.addChild(items)
    items.addChild(schedule)
  
    print("DFS: ")
    rootNode.DFS(rootNode, [])
    print("-------")
    print("BFS: ")
    rootNode.BFS(rootNode)
 

main()




