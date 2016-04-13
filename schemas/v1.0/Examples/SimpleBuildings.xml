<?xml version="1.0" encoding="UTF-8"?>
<!-- Example CityGML dataset illustrating buildings in LOD1 and LOD2. -->
<!-- This instance document refers to the XML Schema definition file ../CityGML.xsd which provides an example CityGML profile definition of the CityGML base profile. -->
<!-- Editors: PD Dr. Gerhard Groeger, Institute for Geodesy and Geoinformation, University of Bonn & -->
<!-- Prof. Dr. Thomas H. Kolbe, Institute for Geodesy and Geoinformation Science, Technical University of Berlin -->
<core:CityModel xmlns="http://www.citygml.org/citygml/profiles/base/1.0" xmlns:core="http://www.opengis.net/citygml/1.0"
    xmlns:bldg="http://www.opengis.net/citygml/building/1.0" xmlns:grp="http://www.opengis.net/citygml/cityobjectgroup/1.0"
    xmlns:tex="http://www.opengis.net/citygml/texturedsurface/1.0" xmlns:gml="http://www.opengis.net/gml"
    xmlns:xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0" xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.citygml.org/citygml/profiles/base/1.0 ../CityGML.xsd">
    <gml:description> Simple example for an XML dataset according to CityGML, the GML application schema of the SIG 3D. This
        dataset contains four parts with different complexities. 1.) Simple building in LOD2 with one textured and one colored
        surface. 2.) Simple building in LOD1 as blocks model without balcony, and the same building with gabled roof and balcony
        in LOD2. 3.) House with gabled roof and garage, represented by two BuildingParts. The common wall surface of the building
        and the garage is defined only once and is in the boundary of one solid, and is re-used by the second solid. 4.) Building
        group consisting of two buildings that have been defined previously. The coordinate reference system is given in DHDN /
        Gauss-Krueger 3 degree (2nd zone) + normal heights above sea level (DHHN92). This system is referred to by
        srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783". Please note that the coordinates actually used in this
        dataset have been trimmed for clarity reasons and thus do not match this CRS. </gml:description>
    <gml:name>3D city model of Samplecity</gml:name>
    <gml:boundedBy>
        <gml:Envelope srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
            <gml:pos srsDimension="3">0.0 0.0 0.0 </gml:pos>
            <gml:pos srsDimension="3">33.0 34.0 2.5</gml:pos>
        </gml:Envelope>
    </gml:boundedBy>
    <core:cityObjectMember>
        <!-- Simple building with gabled roof with two storeys and an address. It is a LOD2 model, because it contains a  roof shape  -->
        <bldg:Building gml:id="Build0815">
            <gml:name>Wirtschafts-_oder_Industriegebaeude_allgemein</gml:name>
            <core:externalReference>
                <core:informationSystem>http://www.adv-online.de</core:informationSystem>
                <!-- Reference to the german cadastral database -->
                <core:externalObject>
                    <core:uri>urn:adv:oid:DEHE123400007001</core:uri>
                    <!-- ID of the object, being unique country-wide -->
                </core:externalObject>
            </core:externalReference>
            <bldg:function>1000</bldg:function>
            <bldg:yearOfConstruction>1985</bldg:yearOfConstruction>
            <bldg:roofType>1030</bldg:roofType>
            <bldg:measuredHeight uom="#m">8.0</bldg:measuredHeight>
            <bldg:storeysAboveGround>2</bldg:storeysAboveGround>
            <bldg:storeyHeightsAboveGround uom="#m">2.5 2.5</bldg:storeyHeightsAboveGround>
            <bldg:lod2Solid>
                <!--simple building with gabled roof-->
                <gml:Solid srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
                    <gml:exterior>
                        <gml:CompositeSurface>
                            <gml:surfaceMember>
                                <tex:TexturedSurface orientation="+">
                                    <!--front surface-->
                                    <gml:baseSurface>
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:posList srsDimension="3"> 1.0 1.0 0.0 3.0 1.0 0.0 3.0 1.0 1.5 2.0 1.0 2.5
                                                        1.0 1.0 1.5 1.0 1.0 0.0 </gml:posList>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:baseSurface>
                                    <tex:appearance>
                                        <tex:SimpleTexture>
                                            <tex:textureMap>FrontTexture096454.jpg</tex:textureMap>
                                            <tex:textureCoordinates> 0.05 0.07 0.95 0.07 0.95 0.5 0.5 1 0.05 0.5 0.05 0.07 </tex:textureCoordinates>
                                            <tex:textureType>specific</tex:textureType>
                                        </tex:SimpleTexture>
                                    </tex:appearance>
                                </tex:TexturedSurface>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <tex:TexturedSurface orientation="+">
                                    <!--back surface-->
                                    <gml:baseSurface>
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">1.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">1.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">2.0 4.0 2.5</gml:pos>
                                                    <gml:pos srsDimension="3">3.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">3.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">1.0 4.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:baseSurface>
                                    <tex:appearance>
                                        <tex:Material>
                                            <tex:ambientIntensity>0.4</tex:ambientIntensity>
                                            <tex:diffuseColor> 0 0 1 </tex:diffuseColor>
                                            <!-- defines blue color -->
                                        </tex:Material>
                                    </tex:appearance>
                                </tex:TexturedSurface>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--ground surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:posList srsDimension="3"> 1.0 1.0 0.0 1.0 4.0 0.0 3.0 4.0 0.0 3.0 1.0 0.0 1.0 1.0
                                                0.0 </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--1st roof surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">2.0 1.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">3.0 1.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">3.0 4.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">2.0 4.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">2.0 1.0 2.5</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--2nd roof surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">2.0 1.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">2.0 4.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">1.0 4.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">1.0 1.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">2.0 1.0 2.5</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--1st side surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">3.0 1.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">3.0 4.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">3.0 4.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">3.0 1.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">3.0 1.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--2nd side surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">1.0 1.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">1.0 1.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">1.0 4.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">1.0 4.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">1.0 1.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:CompositeSurface>
                    </gml:exterior>
                </gml:Solid>
            </bldg:lod2Solid>
        </bldg:Building>
    </core:cityObjectMember>
    <core:cityObjectMember>
        <!--  Simple building represented in LOD1 (as blocks model without balcony) and in LOD2 
			with roof and balcony. One of the roof surfaces is represented explicitly as a thematic surface object (RoofSurface). 
			The function is residential building (1000) and the roof type is 'gabled roof' (1030). Both values are defined in external code lists.-->
        <bldg:Building gml:id="Build0816">
            <gml:name>Villa Kunterbunt</gml:name>
            <bldg:function>1000</bldg:function>
            <bldg:yearOfConstruction>1952</bldg:yearOfConstruction>
            <bldg:roofType>1030</bldg:roofType>
            <bldg:lod1Solid>
                <gml:Solid srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
                    <!--simple blocks model -->
                    <gml:exterior>
                        <gml:CompositeSurface>
                            <gml:surfaceMember>
                                <!--front surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--back surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--ground surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--roof surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--1st side surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--2nd side surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:CompositeSurface>
                    </gml:exterior>
                </gml:Solid>
            </bldg:lod1Solid>
            <bldg:lod2Solid>
                <gml:Solid srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
                    <!-- simple building with gabled roof-->
                    <gml:exterior>
                        <gml:CompositeSurface>
                            <gml:surfaceMember>
                                <!--front surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">32.0 31.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--back surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">32.0 34.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--ground surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--1st roof surface-->
                                <gml:Polygon gml:id="roofsurface4711">
                                    <!-- This polygon will be referenced below -->
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:posList srsDimension="3"> 32.0 31.0 2.5 33.0 31.0 1.5 33.0 34.0 1.5 32.0 34.0 2.5
                                                32.0 31.0 2.5 </gml:posList>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--2nd roof surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">32.0 31.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">32.0 34.0 2.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">32.0 31.0 2.5</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--1st side surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">33.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">33.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!--2nd st side surface-->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 1.5</gml:pos>
                                            <gml:pos srsDimension="3">31.0 34.0 0.0</gml:pos>
                                            <gml:pos srsDimension="3">31.0 31.0 0.0</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:CompositeSurface>
                    </gml:exterior>
                </gml:Solid>
            </bldg:lod2Solid>
            <bldg:outerBuildingInstallation>
                <bldg:BuildingInstallation>
                    <gml:name>The nice balcony to the south</gml:name>
                    <bldg:function>1000</bldg:function>
                    <!--function 1000 of a BuildingInstallation means 'balcony'-->
                    <bldg:lod2Geometry>
                        <!-- The balcony is situated at the 1st  front surface -->
                        <!-- The geometry of the balcony is defined by an aggregation of 3D surfaces. -->
                        <gml:CompositeSurface srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
                            <gml:surfaceMember>
                                <!-- ground surface of the balcony -->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.5 30.5 0.8</gml:pos>
                                            <gml:pos srsDimension="3">31.5 31.0 0.8</gml:pos>
                                            <gml:pos srsDimension="3">32.5 31.0 0.8</gml:pos>
                                            <gml:pos srsDimension="3">32.5 30.5 0.8</gml:pos>
                                            <gml:pos srsDimension="3">31.5 30.5 0.8</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!-- front surface of the balcony -->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.5 30.5 0.8</gml:pos>
                                            <gml:pos srsDimension="3">31.5 30.5 1.3</gml:pos>
                                            <gml:pos srsDimension="3">32.5 30.5 1.3</gml:pos>
                                            <gml:pos srsDimension="3">32.5 30.5 0.8</gml:pos>
                                            <gml:pos srsDimension="3">31.5 30.5 0.8</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!-- 1st side surface of the balcony -->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">31.5 30.5 0.8</gml:pos>
                                            <gml:pos srsDimension="3">31.5 30.5 1.3</gml:pos>
                                            <gml:pos srsDimension="3">31.5 31.0 1.3</gml:pos>
                                            <gml:pos srsDimension="3">31.5 31.0 0.8</gml:pos>
                                            <gml:pos srsDimension="3">31.5 30.5 0.8</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                            <gml:surfaceMember>
                                <!-- 1st side surface of the balcony  -->
                                <gml:Polygon>
                                    <gml:exterior>
                                        <gml:LinearRing>
                                            <gml:pos srsDimension="3">32.5 30.5 0.8</gml:pos>
                                            <gml:pos srsDimension="3">32.5 30.5 1.3</gml:pos>
                                            <gml:pos srsDimension="3">32.5 31.0 1.3</gml:pos>
                                            <gml:pos srsDimension="3">32.5 31.0 0.8</gml:pos>
                                            <gml:pos srsDimension="3">32.5 30.5 0.8</gml:pos>
                                        </gml:LinearRing>
                                    </gml:exterior>
                                </gml:Polygon>
                            </gml:surfaceMember>
                        </gml:CompositeSurface>
                    </bldg:lod2Geometry>
                </bldg:BuildingInstallation>
            </bldg:outerBuildingInstallation>
            <bldg:boundedBy>
                <bldg:RoofSurface>
                    <core:externalReference>
                        <core:informationSystem>http://www.solar-panel.com/database/samplecity</core:informationSystem>
                        <!--  This may be a database, which contains all roof surfaces of a city covered with solar panels -->
                        <core:externalObject>
                            <core:name>roof_10786</core:name>
                            <!-- roof_10786 is the id of the roof surface in the external solar panel database  -->
                        </core:externalObject>
                    </core:externalReference>
                    <bldg:lod2MultiSurface>
                        <gml:MultiSurface>
                            <!-- Reference to a surface which has already been defined in the solid boundary of the outer building shell. -->
                            <gml:surfaceMember xlink:href="#roofsurface4711"/>
                        </gml:MultiSurface>
                    </bldg:lod2MultiSurface>
                </bldg:RoofSurface>
            </bldg:boundedBy>
        </bldg:Building>
    </core:cityObjectMember>
    <core:cityObjectMember>
        <!-- House with saddle back roof and garage, represented by  two BuildingParts. The common wall surface of the building and 
			the garage is shared by both solids realizing a toplogical connection between both parts. -->
        <bldg:Building gml:id="Build0817">
            <bldg:consistsOfBuildingPart>
                <bldg:BuildingPart gml:id="Build0817a">
                    <bldg:function>1000</bldg:function>
                    <bldg:yearOfConstruction>1964</bldg:yearOfConstruction>
                    <bldg:roofType>1030</bldg:roofType>
                    <bldg:storeysAboveGround>2</bldg:storeysAboveGround>
                    <bldg:lod2Solid>
                        <gml:Solid srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
                            <!--Building with gabled roof-->
                            <gml:exterior>
                                <gml:CompositeSurface>
                                    <gml:surfaceMember>
                                        <!--front surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:posList srsDimension="3"> 8.0 2.0 0.0 8.0 4.0 0.0 8.0 4.0 1.5 8.0 3.0 2.5
                                                        8.0 2.0 1.5 8.0 2.0 0.0 </gml:posList>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!-- back surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">5.0 2.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 2.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 3.0 2.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 2.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--ground surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">5.0 2.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 2.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 2.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--1st roof surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">5.0 2.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 2.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 3.0 2.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 3.0 2.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 2.0 1.5</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--2nd roof surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">8.0 3.0 2.5</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 3.0 2.5</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 3.0 2.5</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--1st side surface (not oriented towards the garage)-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">8.0 2.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 2.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 2.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 2.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 2.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--2nd side surface, shares surface with garage geometry-->
                                        <gml:Polygon gml:id="polygon007">
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--2nd side surface, does not share surface with garage geometry-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">5.0 4.0 1.5</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.5</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                </gml:CompositeSurface>
                            </gml:exterior>
                        </gml:Solid>
                    </bldg:lod2Solid>
                </bldg:BuildingPart>
            </bldg:consistsOfBuildingPart>
            <bldg:consistsOfBuildingPart>
                <bldg:BuildingPart gml:id="Build817b">
                    <bldg:function>1630</bldg:function>
                    <!-- Function 1630 means 'garage' -->
                    <bldg:yearOfConstruction>1996</bldg:yearOfConstruction>
                    <bldg:roofType>1000</bldg:roofType>
                    <bldg:storeysAboveGround>1</bldg:storeysAboveGround>
                    <bldg:lod2Solid>
                        <gml:Solid srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
                            <!--garage-->
                            <gml:exterior>
                                <gml:CompositeSurface>
                                    <gml:surfaceMember>
                                        <!--front surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">8.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 5.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 5.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--back surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">6.5 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 5.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 5.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--ground surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">6.5 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 5.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 5.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 0.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--roof surface-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">6.5 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 4.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 5.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 5.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 4.0 1.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--side surface, not oriented towards the building-->
                                        <gml:Polygon>
                                            <gml:exterior>
                                                <gml:LinearRing>
                                                    <gml:pos srsDimension="3">8.0 5.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 5.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 5.0 0.0</gml:pos>
                                                    <gml:pos srsDimension="3">6.5 5.0 1.0</gml:pos>
                                                    <gml:pos srsDimension="3">8.0 5.0 1.0</gml:pos>
                                                </gml:LinearRing>
                                            </gml:exterior>
                                        </gml:Polygon>
                                    </gml:surfaceMember>
                                    <gml:surfaceMember>
                                        <!--2nd side surface, shares surface with building geometry-->
                                        <gml:OrientableSurface orientation="-">
                                            <!-- Surface orientation has to be reversed! -->
                                            <gml:baseSurface xlink:href="#polygon007"/>
                                        </gml:OrientableSurface>
                                    </gml:surfaceMember>
                                </gml:CompositeSurface>
                            </gml:exterior>
                        </gml:Solid>
                    </bldg:lod2Solid>
                </bldg:BuildingPart>
            </bldg:consistsOfBuildingPart>
            <bldg:address>
                <core:Address>
                    <core:xalAddress>
                        <xAL:AddressDetails>
                            <xAL:Country>
                                <xAL:CountryName>Germany</xAL:CountryName>
                                <xAL:Locality Type="Town">
                                    <xAL:LocalityName>Bonn</xAL:LocalityName>
                                    <xAL:Thoroughfare Type="Street">
                                        <xAL:ThoroughfareNumber>172</xAL:ThoroughfareNumber>
                                        <xAL:ThoroughfareName>Meckenheimer Allee</xAL:ThoroughfareName>
                                    </xAL:Thoroughfare>
                                    <xAL:PostalCode>
                                        <xAL:PostalCodeNumber>53115</xAL:PostalCodeNumber>
                                    </xAL:PostalCode>
                                </xAL:Locality>
                            </xAL:Country>
                        </xAL:AddressDetails>
                    </core:xalAddress>
                    <core:multiPoint>
                        <gml:MultiPoint>
                            <gml:pointMember>
                                <gml:Point>
                                    <gml:pos srsDimension="3">6.5 4.0 1.0</gml:pos>
                                </gml:Point>
                            </gml:pointMember>
                        </gml:MultiPoint>
                    </core:multiPoint>
                </core:Address>
            </bldg:address>
        </bldg:Building>
    </core:cityObjectMember>
    <core:cityObjectMember>
        <!--Building group with name 'Scenic view', consisting of the two buildings Build0815 and Build0817. Both buildings are included by reference.-->
        <grp:CityObjectGroup gml:id="Complex113">
            <gml:name>Hotel complex 'Scenic View'</gml:name>
            <grp:function>building group</grp:function>
            <grp:groupMember role="main building" xlink:href="#Build0817"/>
            <grp:groupMember xlink:href="#Build0815"/>
        </grp:CityObjectGroup>
    </core:cityObjectMember>
</core:CityModel>
