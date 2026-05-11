# 🏠 House Price Prediction Model

## 📋 Project Overview

This project implements a **Linear Regression model** to predict house prices in Tehran based on property features and location data. The model employs **target encoding** to transform categorical variables, achieving an impressive **R² score of 0.83** (with tuning achieving up to 0.8674).

## 🎯 Key Features

### Data Processing Pipeline
- **Automated data cleaning** with intelligent filtering to remove outliers and invalid entries
- **Target encoding** for categorical variables to avoid one-hot encoding dimensionality explosion
- **Feature engineering** that captures how amenities impact prices within specific locations

### Target Encoding Strategy

The encoding approach creates features by mapping each categorical value to the mean price of its group:

| Feature | Encoding Method |
|---------|-----------------|
| **Address** | Global mean price per address |
| **Parking** | Mean price for `(parking_status, address)` combination |
| **Room** | Mean price for `(room_count, address)` combination |
| **Elevator** | Mean price for `(elevator_status, address)` combination |
| **Warehouse** | Mean price for `(warehouse_status, address)` combination |

## 📊 Data Filters Applied

The dataset is cleaned using the following criteria:
- ✅ Area between 0 and 350 sqm
- ✅ Area / Room count > 38 sqm per room
- ✅ Room count < 6
- ✅ Address not null

## 🚀 Model Performance

```
R² Score on Test Set: 0.83
Best Tuned R² Score: 0.8674
```

## 📈 Visualizations

The notebook includes comprehensive scatter plots showing relationships between:
- Address encoding vs. Price
- Area vs. Price  
- Parking encoding vs. Price
- Room encoding vs. Price
- Elevator encoding vs. Price
- Warehouse encoding vs. Price

## 🛠️ Technical Stack

- **Python 3**
- **pandas** - Data manipulation and analysis
- **scikit-learn** - Linear Regression, metrics
- **matplotlib** - Data visualization
- **NumPy** - Numerical operations

## 📁 Project Structure

```
├── data/
│   └── House_price.csv          # Input dataset
├── Notebooks
    ├── main.ipynb                    # Jupyter notebook with full implementation
└── requirements.txt              # Python dependencies
```

## 🔧 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Mahan-Pourkami/House_price
cd House_price
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Jupyter notebook**
```bash
jupyter notebook main.ipynb
```

## 📖 Usage

The notebook is organized into clear sections:

1. **Import Libraries** - Load all required packages
2. **Data Loading** - Read CSV and convert string numerical attributes
3. **Data Filtering** - Apply cleaning criteria
4. **Data Review** - Explore neighborhood distributions
5. **Encoding** - Apply target encoding to categorical features
6. **Train-Test Split** - 80/20 split for model evaluation
7. **Visualization** - Scatter plots of all features
8. **Model Training** - Fit Linear Regression
9. **Evaluation** - Calculate R² score

## 💡 Key Insights

### Target Encoding Benefits
- Captures location-specific amenity impacts on price
- Avoids the curse of dimensionality from one-hot encoding
- Preserves relationships between features within the same address

### Suggested Improvements
Adding a **YearBuilt** feature would further improve encodings by:
- Factoring in property age (newer buildings command higher prices)
- Disentangling construction year effects from neighborhood trends
- Separating amenity values from temporal depreciation

## 📊 Sample Output

```
Number of Houses by Neighborhood (Top 20)
[Bar chart visualization]

R² Score: 0.83
```

## 🔮 Future Enhancements

- [ ] Add `YearBuilt` feature for improved accuracy
- [ ] Implement cross-validation for more robust evaluation
- [ ] Experiment with other regression algorithms (Random Forest, XGBoost)
- [ ] Add feature importance analysis
- [ ] Create prediction API endpoint

## 📝 License

This project is available for educational and research purposes.

## 👥 Contributors

Mahan.F.Pourkami

---

**Note**: The model achieves strong performance (0.83 R²) using only location and basic property features, demonstrating the effectiveness of target encoding for categorical variables in real estate price prediction.
