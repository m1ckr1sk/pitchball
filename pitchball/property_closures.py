def typedproperty(name, property_type):
    private_name = '_'+ name
    
    @property
    def _typedproperty(self):
        return getattr(self, private_name)

    @_typedproperty.setter
    def _typedproperty(self, value):
        if not isinstance(value, property_type):
            raise TypeError(f"{name} expected {property_type} got {value}")

        setattr(self, private_name, value)

    return _typedproperty

def roproperty(name):
    private_name = '_'+ name
    
    @property
    def _roproperty(self):
        return getattr(self, private_name)

    return _roproperty