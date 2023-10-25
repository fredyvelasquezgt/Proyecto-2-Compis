import uuid

BOOL_MAX_SIZE = 1
INT_MAX_SIZE = 64
STR_MAX_SIZE_PER_CHAR = 8

class Symbol():

    def __init__(
            self,
            id,
            data_type=None,
            line=None,
            column=None,
            value=None,
            scope=None,
            scope_type=None,
            inherits=None,
            numParams=None,
            paramTypes=None,
            size=None,
            max_size=None,
            address_id=None
        ):
        self.uuid = str(uuid.uuid4()) + "-" + str(id)
        self.id = str(id)
        self.data_type = str(data_type)
        self.line = line
        self.column = column
        self.value = value
        self.scope = scope
        self.scope_type = scope_type
        self.inherits = str(inherits) if inherits else None
        self.numParams = numParams
        self.paramTypes = paramTypes
        self.size = size
        self.max_size = max_size
        self.address_id = address_id

    def keys(self):
        return ["uuid", "id", "data_type", "line", "column", "value", "scope", "scope_type", "inherits", "numParams", "paramTypes", "size", "max_size", "address_id"]

    def values(self):
        line = self.line if self.line != None else ""
        column = self.column if self.column != None else ""
        value = self.value if self.value != None else ""
        scope = self.scope if self.scope != None else ""
        scope_type = self.scope_type if self.scope_type != None else ""
        inherits = self.inherits if self.inherits != None else ""
        numParams = self.numParams if self.numParams != None else ""
        paramTypes = self.paramTypes if self.paramTypes != None else ""
        size = self.size if self.size != None else ""
        max_size = self.max_size if self.max_size != None else ""
        address_id = self.address_id if self.address_id != None else ""

        return [self.uuid, self.id, self.data_type, line, column, value, scope, scope_type, inherits, numParams, paramTypes, size, max_size, address_id]

    def __str__(self):
        return str(self.values())


class SymbolTable():

    def __init__(self):
        self.records = []

    def add(
        self,
        id,
        data_type,
        line=None,
        column=None,
        value=None,
        scope=None,
        scope_type=None,
        inherits=None,
        is_array=False,
        numParams=None,
        paramTypes=None,
        size=None,
        max_size=None,
        address_id=None,
    ):
        if not is_array:

            if str(id) == "self":
                return False, "No es posible usar 'self' como identificador"

            # Default values
            if str(data_type) == "String" and not value:
                value = ""
            elif str(data_type) == "Int" and not value:
                value = 0
            elif str(data_type) == "Bool" and not value:
                value = False
            elif str(data_type) == "class" or str(data_type) == "SELF_TYPE":
                value = "void"
            else:
                if str(data_type) not in self.get_defined_classes():
                    return False, "Class type '{data_type}' no definido".format(data_type=str(data_type))
                value = "void"

            if str(data_type) == "String":
                size = STR_MAX_SIZE_PER_CHAR * len(value)
                max_size = STR_MAX_SIZE_PER_CHAR * len(value)
                max_size = max_size if max_size > 0 else STR_MAX_SIZE_PER_CHAR
            elif str(data_type) == "Int":
                size = value.bit_length()
                max_size = INT_MAX_SIZE
            elif str(data_type) == "Bool":
                size = value.bit_length()
                max_size = BOOL_MAX_SIZE
            else:
                max_size = None

            symbol = Symbol(
                id,
                data_type=data_type,
                line=line,
                column=column,
                value=value,
                scope=scope,
                scope_type=scope_type,
                inherits=inherits,
                numParams=numParams,
                paramTypes=paramTypes,
                size=size,
                max_size=max_size,
                address_id=address_id,
            )

            self.records.append(symbol)

            return True, symbol

    def find(self, id, data_type=None, scope=None, scope_type=None):
        for symbol in self.records:
            if symbol.id == str(id):

                if data_type and scope:
                    if symbol.data_type == str(data_type) and symbol.scope == scope and symbol.scope_type == scope_type:
                        return symbol
                elif data_type:
                    if symbol.data_type == str(data_type):
                        return symbol
                elif scope:
                    if symbol.scope == scope and symbol.scope_type == scope_type:
                        return symbol
                else:
                    return symbol

    def get_defined_classes(self):
        defined_classes = []
        for symbol in self.records:
            if symbol.data_type == "class":
                defined_classes.append(symbol.id)

        return defined_classes
