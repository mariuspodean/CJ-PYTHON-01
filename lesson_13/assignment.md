# Lesson 13 - Inheritance

We have new customers for our Polygons company.
    * They need to create square objects with a certain area
    * They need a method to compute the perimeter only for triangle objects

Requirements:
    * add an alternative constructor to Square class that takes the area as an argument and creates a square object with the apropriate sides 
> example : 
>
>     >> sq = Square.from_area(8)
>     >> print(sq)
>     >> Side 1 with lenght: 2
>     >> Side 2 with lenght: 4
>     >> Side 3 with lenght: 2
>     >> Side 4 with lenght: 4

    * we want to make our perimeter method also available to other shapes in the future. Create a mixin class for perimeter that contains the perimeter method 

    
