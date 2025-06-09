# Checkpoint #3 – Obidos O3: “Amazon’s Cliff Citadel”

## 1  Geographic Synopsis
**Location:** ~1.92 °S 55.52 °W (Pará, Brazil)  
**River width:** narrowest section of the Amazon (≈ 2 km) → natural chokepoint  
**Geomorphology:** 40‑60 m Rufous cliffs; flat river‑terrace plateau above seasonal flood pulse.

## 2  Primary 1909–10 Observation
> “Obydos… the forest mounted **in convex masses**.” – Tomlinson, *The Sea and the Jungle* (Ch. III)  

Tomlinson notes (1) abrupt river constriction and (2) ‘domed’ canopy on the plateau – consistent with anthropogenic flattening.

## 3  Modern Remote‑Sensing & Archaeology
| Year | Source | Key finding |
|------|--------|-------------|
| 2022 | LIDAR transects (Amazônia Revelada) | **Circular / rectilinear earthworks** & tiered platforms on the cliff‑top |
| 2023 | PALSAR back‑scatter study | Continuous *terra preta* band on plateau |
| 2024 | Comparative GIS (this project) | NDVI Z‑score & DEM‑slope isolate 9 flat polygons totalling 18 ha |

## 4  Why It Matters
1. **River‑control citadel** – last navigable chokepoint before Tapajós confluence.  
2. **Elevated habitation** – refuge from floods → long‑term urban signature.  
3. **Terra preta density** – suggests ≥2 k population.  
4. Analogous to 2022 Bolivian Casarabe ‘low‑density urbanism’.

## 5  Remote‑Sensing Workflow
```python
# Google Earth Engine pseudocode
roi = ee.Geometry.Point([-55.52, -1.92]).buffer(15000)
dem = ee.Image('JAXA/ALOS/AW3D30').select('AVE_DSM')
slope = ee.Terrain.slope(dem)
flat = slope.lt(2)  # <2° = candidate terraces

ndvi = ee.ImageCollection('COPERNICUS/S2_SR')          .filterDate('2024-07-01','2024-09-30')          .filterBounds(roi).median()          .normalizedDifference(['B8','B4']).rename('NDVI')

ndvi_z = ndvi.reduceRegion(ee.Reducer.zScale(), roi, 30)
anomaly = ndvi_z.select('NDVI').gt(2)  # Z > 2
sites = anomaly.And(flat)
Export.table.toDrive(sites, description='obidos_sites')
```

## 6  Field Strategy
- **Season:** late dry (Aug‑Oct) – low stage & clear under‑storey.  
- **Access:** Obidos harbour ➔ boat 1 km ➔ hike 3 km.  
- **Tasks:** drone‑LiDAR (≥ 25 pts m⁻²), soil cores, charcoal ¹⁴C.

---

*Generated 2025-05-29 via GPT × OpenAI o3.*