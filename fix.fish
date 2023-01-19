#!/bin/fish
for view_name in (cat empresas/urls.py | grep -P " +name" | tr -d " " | tr "'" " " | awk '{print $2}')
     for update_file in (rg -l "vinculacion:$view_name")
          echo "sed -i \"s|vinculacion:$view_name|empresas:$view_name|g\" $update_file"
     end
end