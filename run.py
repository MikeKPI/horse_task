from time import time
import xls_input
import game

script_start_time = time()

data = xls_input.read()
start = [data['start'][1]-data['tl_corner'][1],
         data['start'][0]-data['tl_corner'][0]]
finish = [data['finish'][1]-data['tl_corner'][1],
          data['finish'][0]-data['tl_corner'][0]]

gl = game.GameLogic(chess_map=game.generate_map(data['board']),
                    start=game.get_position(start[0], start[1]),
                    finish=game.get_position(finish[0], finish[1]),
                    figure=game.models.HorseFigure())

start = time()
try:
    a = gl.play()
    print('Algorithm execution time {}'.format(str(time()-start)))
except game.NoPathFound as e:
    print(e)

xls_input.draw(a)

print('Script execution time {}'.format(str(time()-script_start_time)))