
#load librariess
library(tidyverse)
library(tidymodels)
library(skimr)
library(vip)
library(GGally)
library(caret)


heart_data <- read.csv(file = "/Users/ryanquinnandrews/Desktop/heart.csv", header = TRUE)
heart_data$HeartDiseaseorAttack <- factor(heart_data$HeartDiseaseorAttack, levels = c("1", "0"), labels = c("yes", "no"))
heart_data$Smoker <- factor(heart_data$Smoker, levels = c("1", "0"), labels=c("yes","no"))
heart_data1 <- heart_data[, c("BMI", "Smoker", "MentHlth", "Age", "Education", "Income","HeartDiseaseorAttack")]

# Split data into training and test sets
set.seed(123) 
heart_split <- initial_split(heart_data1, prop = 0.8, strata = HeartDiseaseorAttack)
train_data <- training(heart_split)
test_data <- testing(heart_split)
ctrl <- trainControl(classProbs = TRUE,savePredictions = TRUE,summaryFunction = twoClassSummary)
tree_model = train(HeartDiseaseorAttack ~ ., 
                    data = train_data, 
                   method="rpart",trControl = ctrl,metric="ROC")
tree_model %>%
  predict(test_data)
# Predictions
predicted <- predict(tree_model, newdata = test_data)
conf_matrix <- confusionMatrix(data = predicted, 
                               reference = test_data$HeartDiseaseorAttack, 
                               mode = "prec_recall")
# Lift Curve
lift_result <- data.frame(truth = test_data$HeartDiseaseorAttack)
lift_result$yes <- predict(tree_model, test_data, type = "prob")[,"yes"]
lift_result$no <- predict(tree_model, test_data, type = "prob")[,"no"]
lift_result$predicted <- predict(tree_model, test_data)

gain_curve(lift_result, truth, yes) %>% 
  autoplot()

roc_curve(lift_result, truth, yes) %>% 
  autoplot()

lift_curve(lift_result, truth, yes) %>%
  autoplot()

