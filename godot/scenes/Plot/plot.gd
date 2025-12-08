extends Node2D
class_name Plot
var Crop := preload("res://scenes/Crop/crop.tscn")
var rng := RandomNumberGenerator.new()

var num_plots = 5

func _ready():
	var plot_width = get_viewport_rect().size.x
	var plot_height = get_viewport_rect().size.y / num_plots
	var y_position = 200
	
	for i in range(num_plots):
		var crop1 = Crop.instantiate()
		crop1.t1_seed_value = rng.randi_range(5, 20)
		crop1.t2_seed_value = rng.randi_range(5, 20)
		crop1.position = Vector2(200, y_position)
		add_child(crop1)
		
		var crop2 = Crop.instantiate()
		crop2.t1_seed_value = rng.randi_range(5, 20)
		crop2.t2_seed_value = rng.randi_range(5, 20)
		crop2.position = Vector2(400, y_position)
		add_child(crop2)
		
		crop1.target_crop = crop2
		crop2.target_crop = crop1
		
		y_position += 200
