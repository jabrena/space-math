#cas
def get_infos():
  import ti_graphics, ti_system
  fnop = lambda : None
  screen_w, screen_h, screen_y0, font_w, font_h, poly_set_pixel, poly_fill_rect, poly_draw_ellipse, poly_fill_circle, poly_get_key, poly_draw_string = 320, 210, 30, 10, 15, fnop, fnop, fnop, fnop, ti_system.wait_key, fnop
  def poly_fill_rect(x, y, w, h, c):
    ti_graphics.setColor(c)
    ti_graphics.fillRect(x, y + screen_y0, w, h)
  def poly_set_pixel(x, y, c):
    ti_graphics.setPixel(x, y + screen_y0, c)
  def poly_draw_ellipse(x, y, rx, ry, c):
    ti_graphics.setColor(c)
    x0, y0 = x - rx, y - ry
    for dy in range(1 + (y0 > int(y0))):
      for dx in range(1 + (x0 > int(x0))):
        ti_graphics.drawArc(x0 + dx, y0 + dy + screen_y0, 2 * rx, 2 * ry, 0, 3600)
  def poly_fill_circle(x, y, r, c):
    ti_graphics.setColor(c)
    ti_graphics.fillCircle(xx, y + screen_y0, r)
  def poly_draw_string(s, x, y, cf, cb):
    poly_fill_rect(x, y, font_w, font_h, cb)
    ti_graphics.setColor(cf)
    ti_graphics.drawString(s, x, y + screen_y0) 
    

  return screen_w, screen_h, font_h, poly_set_pixel, poly_fill_rect, poly_draw_ellipse, poly_fill_circle, poly_draw_string, poly_get_key


