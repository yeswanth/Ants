def ant_map_tuple_conversion_hook(obj) :
    modified_obj = {}
    for key in obj :
	if key in ["hills", "walls"] :
	    val = [tuple(l) for l in obj[key]]
	    modified_obj[key] = val
	else :
	    modified_obj[key] = obj[key]
    return modified_obj
