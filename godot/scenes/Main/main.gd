extends Node2D

var Plot := preload("res://scenes/Plot/plot.tscn")

var target_crop: Crop

var num_plots = 5

func _ready():
	var plot = Plot.instantiate()
	add_child(plot)
