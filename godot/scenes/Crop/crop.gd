extends Node2D
class_name Crop
var rng := RandomNumberGenerator.new()

var t1_seed_value: int = 0
var t2_seed_value: int = 0
var t3_seed_value: int = 0
var t4_seed_value: int = 0
var crop_color: Color

var target_crop: Crop

var crop_status = 'Alive'

func _ready():
	rng.randomize()
	
	var sprite := $Sprite2D
	var collision: CollisionShape2D = $Area2D/CollisionShape2D
	
	var keys = Constants.CROP.keys()
	var crop_type = keys[rng.randi_range(0, keys.size() - 1)]
	crop_color = Constants.CROP[crop_type]
	
	$Sprite2D.modulate = crop_color
	
	$Label.text = 'T1: ' + str(t1_seed_value) + ' lifeforce\n' + 'T2: ' + str(t1_seed_value) + ' lifeforce\n'
	var label: Label = $Label
	
	var scale_factor = 0.1
	sprite.scale = Vector2(scale_factor, scale_factor)
	
	if sprite.texture:
		var texture_size = sprite.texture.get_size()
		
		var height = sprite.texture.get_height() * sprite.scale.y
		label.position = Vector2(0, height - 10)
	
		if collision.shape == null:
			collision.shape = RectangleShape2D.new()
		
		collision.shape.size = texture_size * scale_factor

func update_label():
	$Label.text = 'T1: ' + str(t1_seed_value) + ' lifeforce\n' + 'T2: ' + str(t1_seed_value) + ' lifeforce\n'
	
func update_color_wilted():
	$Sprite2D.modulate = Color(.25, .25, .25)

func _on_area_2d_mouse_entered() -> void:
	if self.crop_status != 'Wilted':
		$Sprite2D.modulate = Color(0.278, 1.0, 0.0, 1.0)

func _on_area_2d_mouse_exited() -> void:
	if self.crop_status != 'Wilted':
		$Sprite2D.modulate = crop_color

func _on_area_2d_input_event(viewport: Node, event: InputEvent, shape_idx: int) -> void:
	if self.crop_status != 'Wilted':
		if event is InputEventMouseButton:
			if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
				if target_crop.crop_status != 'Wilted':
					target_crop.t1_seed_value += 5
					target_crop.update_label()
				
				self.update_color_wilted()
				self.t1_seed_value = 0
				self.crop_status = 'Wilted'
				self.update_label()
