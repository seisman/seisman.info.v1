GeoTiff格式转GMT netCDF格式
###########################

:date: 2014-01-11 00:41
:author: SeisMan
:category: GMT
:tags: 格式转换, GMT5
:slug: convert-geotiff-to-gmt

`GDAL`_\ 提供了不少小工具，其中， ``gdal_translate`` 可用于网格数据的格式转换。

下面的命令可以将GeoTiff格式的数据转换为GMT可识别的netCDF格式::

    gdal_translate -of GMT srtm_56_05.tif srtm_56_05.nc

``gdal_translate`` 的语法如下：

::

    Usage: gdal_translate [--help-general] [--long-usage]
           [-ot {Byte/Int16/UInt16/UInt32/Int32/Float32/Float64/
                 CInt16/CInt32/CFloat32/CFloat64}] [-strict]
           [-of format] [-b band] [-mask band] [-expand {gray|rgb|rgba}]
           [-outsize xsize[%] ysize[%]]
           [-unscale] [-scale[_bn] [src_min src_max [dst_min dst_max]]]* [-exponent[_bn] exp_val]*
           [-srcwin xoff yoff xsize ysize] [-projwin ulx uly lrx lry] [-epo] [-eco]
           [-a_srs srs_def] [-a_ullr ulx uly lrx lry] [-a_nodata value]
           [-gcp pixel line easting northing [elevation]]*
           [-mo "META-TAG=VALUE"]* [-q] [-sds]
           [-co "NAME=VALUE"]* [-stats] [-norat]
           src_dataset dst_dataset

``-of`` 后接要转换的数据格式，使用 ``gdal_translate --long-usage``\ 可以看到，支持的格式如下：

::

      VRT: Virtual Raster
      GTiff: GeoTIFF
      NITF: National Imagery Transmission Format
      HFA: Erdas Imagine Images (.img)
      ELAS: ELAS
      AAIGrid: Arc/Info ASCII Grid
      DTED: DTED Elevation Raster
      PNG: Portable Network Graphics
      JPEG: JPEG JFIF
      MEM: In Memory Raster
      GIF: Graphics Interchange Format (.gif)
      FITS: Flexible Image Transport System
      XPM: X11 PixMap Format
      BMP: MS Windows Device Independent Bitmap
      PCIDSK: PCIDSK Database File
      PCRaster: PCRaster Raster File
      ILWIS: ILWIS Raster Map
      SGI: SGI Image File Format 1.0
      SRTMHGT: SRTMHGT File Format
      Leveller: Leveller heightfield
      Terragen: Terragen heightfield
      GMT: GMT NetCDF Grid Format
      netCDF: Network Common Data Format
      HDF4Image: HDF4 Dataset
      ERS: ERMapper .ers Labelled
      JPEG2000: JPEG-2000 part 1 (ISO/IEC 15444-1)
      FIT: FIT Image
      RMF: Raster Matrix Format
      RST: Idrisi Raster A.1
      INGR: Intergraph Raster
      GSAG: Golden Software ASCII Grid (.grd)
      GSBG: Golden Software Binary Grid (.grd)
      R: R Object Data Store
      PNM: Portable Pixmap Format (netpbm)
      ENVI: ENVI .hdr Labelled
      EHdr: ESRI .hdr Labelled
      PAux: PCI .aux Labelled
      MFF: Vexcel MFF Raster
      MFF2: Vexcel MFF2 (HKV) Raster
      BT: VTP .bt (Binary Terrain) 1.3 Format
      IDA: Image Data and Analysis
      USGSDEM: USGS Optional ASCII DEM (and CDED)
      ADRG: ARC Digitized Raster Graphics
      BLX: Magellan topo (.blx)
      Rasterlite: Rasterlite
      SAGA: SAGA GIS Binary Grid (.sdat)

.. _GDAL: http://www.gdal.org/
