from __future__ import annotations
from dataclasses import dataclass

from copy import deepcopy

from mountain import Mountain

from typing import TYPE_CHECKING, Union

from data_structures.linked_stack import LinkedStack

# Avoid circular imports for typing.
if TYPE_CHECKING:
    from personality import WalkerPersonality


@dataclass
class TrailSplit:
    """
    A split in the trail.
       ___path_top____
      /               \
    -<                 >-path_follow-
      \__path_bottom__/
    """

    path_top: Trail
    path_bottom: Trail
    path_follow: Trail

    def remove_branch(self) -> TrailStore:
        """
        Removes the branch, should just leave the remaining following trail.
        
        Args:
        - None

        Returns:
        - An instance of the path_follow of the trail
        """
        return self.path_follow.store   

@dataclass
class TrailSeries:
    """
    A mountain, followed by the rest of the trail

    --mountain--following--

    """

    mountain: Mountain
    following: Trail

    def remove_mountain(self) -> TrailStore:
        """
        Removes the mountain at the beginning of this series.
        
        Args:
        - None

        Returns:
        - An instance of the following of the mountain
        """
        return self.following.store

    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """
        Adds a mountain in series before the current one.

        Args:
        - mountain: the mountain to be added

        Returns:
        - A TrailSeries instance in which a mountain has been a mountain has been added before the current one
        """
        return TrailSeries(mountain, Trail(TrailSeries(self.mountain, self.following)))

    def add_empty_branch_before(self) -> TrailStore:
        """
        Adds an empty branch, where the current trailstore is now the following path.
        
        Args:
        - None

        Returns:
        - A TrailSplit instance in which an empty branch is added before the current trailstore
        """
        return TrailSplit(Trail(None), Trail(None), Trail(TrailSeries(self.mountain, self.following)))

    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """
        Adds a mountain after the current mountain, but before the following trail.
        
        Args:
        - mountain: the mountain to be added

        Returns:
        - A TrailSeries instance in which a mountain is added after the current mountain and before the following trail
        """
        return TrailSeries(self.mountain, Trail(TrailSeries(mountain, self.following)))

    def add_empty_branch_after(self) -> TrailStore:
        """
        Adds an empty branch after the current mountain, but before the following trail.
        
        Args:
        - None

        Returns:
        - A TrailSeries instance in which an empty branch was added after the current mountain and after the following trail
        """
        return TrailSeries(self.mountain, Trail(TrailSplit(Trail(None), Trail(None), self.following)))

TrailStore = Union[TrailSplit, TrailSeries, None]

@dataclass
class Trail:

    store: TrailStore = None

    def add_mountain_before(self, mountain: Mountain) -> Trail:
        """
        Adds a mountain before everything currently in the trail.
        
        Args:
        - mountain: the mountain to be added

        Returns:
        - A Trail instance in which a mountain is added before everything else
        """
        return Trail(TrailSeries(mountain, self))

    def add_empty_branch_before(self) -> Trail:
        """
        Adds an empty branch before everything currently in the trail.
        
        Args:
        - None

        Returns:
        - A Trail instance in which an empty branch is added before everything else
        """
        return Trail(TrailSplit(Trail(None), Trail(None), self))

    def follow_path(self, personality: WalkerPersonality) -> None:
        """
        Follow a path and add mountains according to a personality.

        Args:
        - personality: Type WalkerPersonality that is used for select_branch and add_mountain
        
        Returns:
        - None

        Complexity:
        - Worst case: O(n), where n is the amount of mountains in the trail, considering the Trail contains a large number of 
          mountains. 
        - Best case: O(n), where n is the amount of mountains in the trail, considering the Trail contains a large number of 
          mountains
          following the conditions.
        """

        # Create a linkedstack from ADT LinkedStack
        path_stack = LinkedStack() # O(1)
        
        # Current trail is firstly set to self
        current_trail = self # O(1)

        # While loop that keeps going until the end of the path
        while current_trail != None or len(path_stack) != 0 : # O(n)

            # If the current trail is a Trail, change the trail to what is stored inside the Trail
            if isinstance(current_trail, Trail) : # O(1)
                current_trail = current_trail.store # O(1)

            # If the current trail is a TrailSeries, add the mountain and change the trail to it's following
            elif isinstance(current_trail, TrailSeries) : # O(1)
                personality.add_mountain(current_trail.mountain) # O(1)
                current_trail = current_trail.following # O(1)
            
            # If the current trail is a TrailSplit, push the trail to the created path_stack and change the trail accordingly based on the personality
            elif isinstance(current_trail, TrailSplit) : # O(1)
                path_stack.push(current_trail) # O(1)

                if personality.select_branch(current_trail.path_top, current_trail.path_bottom) : # O(1)
                    chosen_path = current_trail.path_top # O(1)
                else : # O(1)
                    chosen_path = current_trail.path_bottom # O(1)

                current_trail = chosen_path.store # O(1)

            # By the end of one trailsplit, the trail is set to the path_follow of the first element in the path_stack
            else : # O(1)
                element = path_stack.peek() # O(1)
                current_trail = element.path_follow.store # O(1)
                path_stack.pop() # O(1)

    def collect_all_mountains(self) -> list[Mountain]:
        """
        Returns a list of all mountains on the trail.

        Args:
        - None

        Returns:
        - list_mountains: list of all the mountains on the trail

        Complexity:
        - Worst case: O(n), where n is the amount of times it loops, based on total number of mountains and branches combined.
        - Best case: O(n), where n is the amount of times it loops, based on total number of mountains and branches combined.
        """
        
        # Current trail is firstly set to self
        current_trail = self # O(1)

        # Create list_mountains for storing all the mountains, and create split_mountain_list to store the paths during trailsplit
        list_mountains = [] # O(1)
        split_mountain_list = [] # O(1)

        # While loop that keeps going until all the mountains have been stored
        while current_trail != None : # O(n)

            # If the current trail is a Trail, change the trail to what is stored inside the trail
            if isinstance(current_trail, Trail) : # O(1)
                current_trail = current_trail.store # O(1)

            # If the current trail is a TrailSeries, append the mountain into the list and change the trail to it's following
            elif isinstance(current_trail, TrailSeries) : # O(1)
                list_mountains.append(current_trail.mountain) # O(1)
                current_trail = current_trail.following # O(1)
                
            # If the current trail is a TrailSplit, recurse through all the paths in the trailsplit
            elif isinstance(current_trail, TrailSplit) : # O(1)
                split_mountain_list.extend([current_trail.path_top, current_trail.path_bottom, current_trail.path_follow]) # O(1)

                for each_trail in split_mountain_list :# O(1)
                    if each_trail != None : # O(1)
                        list_mountains.extend(each_trail.collect_all_mountains()) # O(1)

                current_trail = None # O(1)

        return list_mountains # O(1)

    def length_k_paths(self, k) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        """
        Returns a list of all the possible paths with the length of k.
        """

        def collect_all_paths(current_trail: TrailStore|Trail, path_list: list, all_paths: list, path_stack: LinkedStack) -> list[list[Mountain]] :
            """
            Collects all the possible paths in the trail

            Args:
            - current_trail: the current trail being followed
            - path_list: list of the mountains for the current path
            - all_paths: list of all the paths in the trail
            - path_stack: ADT LinkedStack to store store the trail when a TrailSplit is met

            Returns:
            - all_paths: list of all the possible paths in the trail

            Complexity:
            - Worst case: O(2^n), where n is the number of mountains in the list, which occurs when the trail contains one or
                          more trailsplits, so recursion was done for both path_top and path_bottom. 
            - Best case: O(n), where n is the number of mountains and branches, which occurs when no trailsplit was met, so 
                         this function only runs a number of times according to the total amount of mountains and brances.
            """

            # If the end of the path has been reached, append the path of mountains into the list of all the paths, and return
            if (current_trail == None and len(path_stack) == 0) : # O(1)
                all_paths.append(path_list) # O(1)
                return # O(1)
            
            # If the current trail is a Trail, recurse through the function again, but with what is stored inside the trail
            if isinstance(current_trail, Trail) : # O(1)
                collect_all_paths(current_trail.store, path_list, all_paths, path_stack) # O(1)

            # If the current trail is TrailSeries, add the mountain into the current path, and recurse through the function with the trail's following
            elif isinstance(current_trail, TrailSeries) : # O(1)
                path_list.append(current_trail.mountain) # O(1)
                collect_all_paths(current_trail.following, path_list, all_paths, path_stack) # O(1)

            # If the current trail is a TrailSpit, push the trail to the path stack, and recurse through the function with both the path top and path bottom of the trailsplit, with the deepcopies of the path list and path stack
            elif isinstance(current_trail, TrailSplit) : # O(1)
                path_stack.push(current_trail) # O(1)

                collect_all_paths(current_trail.path_top, deepcopy(path_list), all_paths, deepcopy(path_stack)) # O(n)
                collect_all_paths(current_trail.path_bottom, deepcopy(path_list), all_paths, deepcopy(path_stack)) # O(n)

            # By the end of one trailsplit, recurse through the function with the path follow of the first element in path stack
            else : # O(1)
                element = path_stack.peek() # O(1)
                new_trail = element.path_follow.store # O(1)
                path_stack.pop() # O(1)

                collect_all_paths(new_trail, path_list, all_paths, path_stack) # O(1)

            # Returns the path list containing all the possible paths in the trail
            return all_paths # O(1)

        # Call the created function, with the trail set to self, other appropriate parameters
        all_possible_paths = collect_all_paths(self, [], [], LinkedStack()) 

        # Initialize an empty list first to store all the paths with a specific number of mountains
        k_path = [] # O(1)

        # Loop through each possible path, and append the path when the number of mountains in the path matches k
        for each_path in all_possible_paths : # O(n)
            if len(each_path) == k : # O(1)
                k_path.append(each_path) # O(1)

        return k_path # O(1)

if __name__ == "__main__" :
    pass