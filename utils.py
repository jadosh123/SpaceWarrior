def collision_detection(entity_list, proj_list):
    x_collision = False
    y_collision = False

    for entity in entity_list:
        for projectile in proj_list:
            # Ranges for each projectile and entity
            proj_start_x = projectile.rect.x
            proj_end_x = projectile.rect.x + projectile.rect.width
            proj_start_y = projectile.rect.y
            proj_end_y = projectile.rect.y + projectile.rect.height
            ent_start_x = entity.rect.x
            ent_end_x = entity.rect.x + entity.rect.width
            ent_start_y = entity.rect.y
            ent_end_y = entity.rect.y + entity.rect.height

            # Check for horizontal overlap in bounding boxes x and y
            if (
                proj_start_x >= ent_start_x and proj_start_x <= ent_end_x
                or
                proj_end_x >= ent_start_x and proj_end_x <= ent_end_x
                or
                proj_start_x <= ent_start_x and proj_end_x >= ent_end_x
            ):
                x_collision = True

            if (
                proj_start_y >= ent_start_y and proj_start_y <= ent_end_y
                or
                proj_end_y >= ent_start_y and proj_end_y <= ent_end_y
                or
                proj_start_y <= ent_start_y and proj_end_y >= ent_end_y
            ):
                y_collision = True

            if x_collision and y_collision:
                projectile.kill()
                entity.kill()
                return
            else:
                x_collision = False
                y_collision = False


def mouse_hovering(mouse_pos, sprite):
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]

    start_sprite_x = sprite.rect.x
    start_sprite_y = sprite.rect.y
    end_sprite_x = sprite.rect.x + sprite.rect.width
    end_sprite_y = sprite.rect.y + sprite.rect.height

    if (
        start_sprite_x <= mouse_pos_x <= end_sprite_x
        and
        start_sprite_y <= mouse_pos_y <= end_sprite_y
    ):
        sprite.update(True)
        return True
    else:
        sprite.update(False)
        return False
