def predict_and_save(best_result, test_df):
        print("\nMelhor modelo:")
        print(f"{best_result['model_name']} - RMSE: {best_result['rmse']:.2f}, MAE: {best_result['mae']:.2f}, R2: {best_result['r2']:.3f}")

        model = best_result.get("model")
        predicts = model.predict(test_df)

        test_df['Predicted_Price'] = predicts
        test_df.to_excel('data/test_set_with_predictions.xlsx', index=False)
