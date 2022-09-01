class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # topological sort
        
        n = len(recipes)
        in_degrees = dict()
        graph = collections.defaultdict(list)
        
        for recipe, ingredient in zip(recipes, ingredients):
            in_degrees[recipe] = len(ingredient)
            for material in ingredient:
                graph[material].append(recipe)
        
        q = []
        for supply in supplies:
            for made in graph[supply]:
                in_degrees[made] -= 1
                if in_degrees[made] == 0:
                    q.append(made)
        
        makeable = []
        for supply in q:
            makeable.append(supply)
            for made in graph[supply]:
                in_degrees[made] -= 1
                if in_degrees[made] == 0:
                    q.append(made)
        
        return makeable

