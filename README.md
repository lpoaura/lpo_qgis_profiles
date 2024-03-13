# Demonstration profiles to be deployed with QDT

pensée a écrire le read me ...

## Naturaliste

Some of customizations to make it recognizable:

- blablabla
![QGIS UI - QDT demo profile](https://github.com/Guts/qgis-deployment-cli/blob/main/docs/static/examples_profiles_qdt-demo_qgis_ui.png?raw=true)

Splash screen:
![QGIS splash screen - QDT demo profile](./profiles/demo/images/splash.png)

As QDT developer, you might want to launch QGIS with this profile to edit or check it:

```sh
qgis --profile "demo" --profiles-path examples/
```

----

## Dev

![QGIS splash screen - QDT viewer profile](./profiles/Viewer%20Mode/images/splash.png)

As QDT developer, you might want to launch QGIS with this profile to edit or check it:

```sh
qgis --profile "Viewer Mode" --profiles-path examples/
```

VSCode extension required:

- https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml
