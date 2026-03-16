class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        
        original = image[sr][sc]
        
        # If the starting color is already the target color
        if original == color:
            return image
        
        def dfs(r, c):
            
            # Check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            # Only continue if pixel matches original color
            if image[r][c] != original:
                return
            
            # Change color
            image[r][c] = color
            
            # Explore neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        
        return image