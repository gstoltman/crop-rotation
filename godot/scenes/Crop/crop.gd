extends Node2D
class_name Crop
var seed_value: int = 0
var target_crop: Crop

var original_modulate: Color

func _ready():
	var sprite := $Sprite2D
	var collision: CollisionShape2D = $Area2D/CollisionShape2D
	
	$Label.text = str(seed_value) + ' lifeforce'
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
		
	original_modulate = $Sprite2D.modulate

func update_label():
	$Label.text = str(seed_value) + " lifeforce"
	
func update_color_wilted():
	$Sprite2D.modulate = Color(.5, .5, .5)

func _on_area_2d_mouse_entered() -> void:
	$Sprite2D.modulate = Color(1.0, 0.8, 0.8)

func _on_area_2d_mouse_exited() -> void:
	$Sprite2D.modulate = original_modulate

func _on_area_2d_input_event(viewport: Node, event: InputEvent, shape_idx: int) -> void:
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			seed_value += 5
			update_label()
			
			if target_crop != null:
				target_crop.update_color_wilted()
				target_crop.seed_value = 0
				target_crop.update_label()
