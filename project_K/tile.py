from pico2d import *

class TileMap:

    def get_tile_image_rect(self, id):
        y = self.tile_rows - id // self.tile_cols - 1
        x = id % self.tile_cols
        return self.image_margin+x*(self.tile_width+self.image_spacing), \
               self.image_margin+y*(self.tile_height+self.image_spacing), \
               self.tile_width, self.tile_height

    def draw_to_origin(self, left, bottom, w=None, h=None):
        if w == None and h == None:
            w,h = self.map_width, self.map_height

        for y in range(h):
            for x in range(w):
                id = self.map2d[y][x]
                self.tileset_image.clip_draw_to_origin(*self.get_tile_image_rect(id), x=(x+left)*self.tile_width, y=(y+bottom)*self.tile_height)


    def clip_draw_to_origin(self, left, bottom, width, height, target_left, target_bottom, w=None, h=None):
        if w == None and h == None:
            w, h = width, height

        for y in range(h):
            for x in range(w):
                id = self.map2d[bottom+y][left+x]
                self.tileset_image.clip_draw_to_origin(*self.get_tile_image_rect(id), x=(x+target_left)*self.tile_width, y=(y+target_bottom)*self.tile_height)

