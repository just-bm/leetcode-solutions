class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        hashmap = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        res = []
        made_recipe = True  # Flag to track progress

        while made_recipe:  # Keep checking until no new recipes are made
            made_recipe = False
            for i in recipes:
                if i not in res:  # Avoid duplicate processing
                    fl = 0
                    for ap in hashmap[i]:
                        if ap not in supplies:
                            fl = 1
                            break
                    
                    if fl == 0:
                        res.append(i)
                        supplies.add(i)  # Add only if successfully made
                        made_recipe = True  # Track progress to continue checking

        return res
