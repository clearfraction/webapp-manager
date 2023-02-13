# webapp-manager

To test the package, unpack the latest RPM artifact to `/tmp` and run it:

```
sudo glib-compile-schemas /tmp/usr/share/glib-2.0/schemas/
GSETTINGS_SCHEMA_DIR=/tmp/usr/share/glib-2.0/schemas GI_TYPELIB_PATH=/tmp/usr/lib64/girepository-1.0 LD_LIBRARY_PATH=/tmp/usr/lib64/ PYTHONPATH=/tmp/usr/lib/webapp-manager /tmp/usr/lib/webapp-manager/webapp-manager.py
```
