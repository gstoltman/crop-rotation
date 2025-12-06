extends Node2D

var rng := RandomNumberGenerator.new()
var Crop := preload("res://scenes/Crop/crop.tscn")
var target_crop: Crop


func _ready():
	print('main ready')
	print("Window size: ", get_viewport_rect().size)
	rng.randomize()
	
	var crop1 = Crop.instantiate()
	crop1.seed_value = rng.randi_range(5, 20)
	crop1.position = Vector2(100, 100)
	add_child(crop1)
	
	var crop2 = Crop.instantiate()
	crop2.seed_value = rng.randi_range(5, 20)
	crop2.position = Vector2(200, 100)
	add_child(crop2)
	
	crop1.target_crop = crop2
	crop2.target_crop = crop1
