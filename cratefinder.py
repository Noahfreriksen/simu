def boxfinder (self, X_cor, Y_cor, aantal_cor, box_W, box_L)
import math

max_anglechange = 5
max_length_error = 10 
found_box_parts

for i in range(aantal_cor):
    found_box_parts[i] = 0

for i in range(aantal_cor):
    j=i
    while ( ( (Y_cor[j] - Y_cor[j+1] ) / (Y_cor[j] - Y_cor[j+1] ) ) - ( (Y_cor[j+1] - Y_cor[j+2] ) / (Y_cor[j+1] - Y_cor[j+2] ) )) < max_anglechange :
        j=j+1
    
    distance =  math.sqrt( (X_cor[j] - X_cor[i])**2 + (Y_cor[j] - Y_cor[i])**2 )

    error_w = math.fabs( distance - box_W)
    error_l = math.fabs( distance - box_L)

    if error_w <= max_length_error | error_l <= max_length_error :
        for n in range(i , j):
        found_box_parts[n] = 1

return found_box_parts
    



