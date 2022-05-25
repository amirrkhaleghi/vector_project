    def inner(self, vec1):
        vec = Vector.lenth(self)
        return [(vec[0] * vec1[0]) + (vec[1] * vec1[1])]

    def cart_convert(self):
        vec = Vector.lenth(self)
        r = math.sqrt((vec[0]**2 + vec[1]**2))
        O = math.degrees(math.atan(vec[1]/vec[0]))
        return [(r * math.cos(O)), (r * math.sin(O))]
    
    
    def toUnitVec(self):
        vec = Vector.lenth(self)
        r = math.sqrt((vec[0]**2 + vec[1]**2))
        return f"{vec[0]}i/{r} + {vec[1]}j/{r}"