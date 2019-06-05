# Apps Database

GNOME3-HIG/GTK3 community applications database

# Adding apps to repository

Apps must meet [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/stable/).

## Files structure
```
|-- appname
   |-- description.md (app description)
   |-- icon.svg (app icon)   
   |-- metadata.yml (app metadata)
   |-- screenshot.png (app screenshot)
```

**metadata.yml** example:
```
name: App Name
description: Short and beautiful app description
categories: [AudioVideo, Audio, Video, Development, Education, Game, Graphics, Network, Office, Science, Settings, System, Utility]
website: https://example.com
install-flatpak: http://link.to.flatpakref
```

**description.md** example:
```
Long description about what this app do.

## Features
* Nice list of app features
* ;)

## More
Other useful sections are admitted
```

## Specifications:

### metadata.yml:

#### name
Correctly formatted application's name.

#### description
Short application's description, usually the one provided on `.desktop` file.

#### categories
List of application's categories. To find a list of valid categories, take a look into [FreeDesktop.org's Desktop Menu Specification](https://standards.freedesktop.org/menu-spec/latest/apa.html).

#### website *(optional)*
Application's website link, with the following format (https://example.com).

#### install-flatpak *(optional)*
URL to .flatpakref file. Only if app provide flatpak installation method

> Currently only Flatpak support in mind, but we don't discard support others distro-agnostic/universal packaging systems.

> No future plans to support distro-specific installation methods.


### description.md:
Markdown file with extensive application's description.

### icon.svg:
SVG application's icon. The icon must be Optimised (we recommend [Scour](https://github.com/scour-project/scour)).

### screenshot.png:
Application's screenshot.
* Screenshot must be in png format (with alpha channel).
* App must be using gtk theme Adwaita (dark variant is allowed).
* App must be using Adwaita icon theme.
* Cursor must be hidden
* Screenshots must include window borders.
