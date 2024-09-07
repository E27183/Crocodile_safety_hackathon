# GovHack - Northern Territory Crocodile Awareness Platform

This project aims to design and develop a comprehensive platform that leverages modern technology to provide timely, accurate information and analysis about crocodile activity, enhancing public safety for both residents and tourists in the Northern Territory.

## Components of the Solution
### Front-End Interface
**Map Integration**: The crocodile alert system will integrate with popular mapping services such as Google Maps or Waze APIs.
**Crocodile Activity Mapping**: The map will feature color-coded areas indicating varying levels of crocodile activity. The color gradient will represent the danger level—e.g., light green for low risk, yellow for moderate risk, and red for high risk.
**User Submissions**: Users can report crocodile sightings via a simple submission form on the platform. This data will be used to update the risk levels and provide real-time information.
**Alert System**: The interface will have an alert system that sends notifications to users about nearby crocodile sightings, changes in risk levels, and important messages from the NT government.

### Back-End System
**Machine Learning Model**: The system will employ machine learning algorithms to analyse historical data and predict crocodile activity. The model will consider various factors, including:
 - Water Levels: Seasonal variations in water levels can affect crocodile behaviour. Higher water levels may expand their habitat and increase their movement, while lower water levels might concentrate their activity in specific areas.
 + Temperature: Saltwater crocodiles are highly sensitive to changes in water temperature. Warmer water temperatures typically increase their activity levels, while cooler temperatures may reduce their movement and feeding behaviour.
 + Breeding Seasons: During breeding seasons, crocodile activity may increase.
**Database Management**: A robust data warehouse will store historical sightings, environmental data (water levels and temperature), and user submissions. This data will be used to refine predictions and improve the accuracy of the risk assessment.

### Data Collection and Crowdsourcing
**Crowdsourcing Integration**: The platform encourages users to contribute sightings and other relevant data. Crowdsourced information will be validated by other users and incorporated into the system.
**Social Media Integration**: The platform could integrate with social media to create data points based on hashtags and photos for validation.
**Additional Technologies**: Consideration for integrating additional technologies to improve data accuracy:
 - Cameras: Night vision trail cameras can be strategically placed in key areas to monitor real-time crocodile presence and behaviour.
 + Acoustic Sensors: These sensors can help identify crocodile movements and vocalizations, providing additional data on their activity patterns.
 + Environmental Sensors: Deploy sensors to monitor water levels, temperature, and other environmental factors that affect crocodile behaviour.

## Datasets
- NT Crocodile Capture Zones and Daily Count
- Crocodile Monitoring Survey
- Daily Maximum Temperature, Bureau of Meteorology - All years of data; Stations: Borroloola Airport, Darwin Airport, Gove Airport Met Office, Tindal RAAF
- Measured Water Level, Department of Environment, Parks and Water Security, Northern Territory Government; Locations: Rapid Crk - D/S McMillans Road, Katherine River - Railway Bridge, Mcarthur River - Borroloola Xng

## Data Story
By leveraging the NT Crocodile datasets, we’ve developed a detailed map that showcases regions with high crocodile capture rates. This map visualises the frequency and distribution of crocodile activities across the Northern Territory. Through analysis of these datasets, we can assess and predict risk levels for both visitors and local residents. This approach not only improves crocodile management practices but also significantly enhances overall safety in the Northern Territory.











