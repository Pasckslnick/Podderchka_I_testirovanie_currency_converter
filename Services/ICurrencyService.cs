using CurrencyConverter.Models;

namespace CurrencyConverter.Services;

public interface ICurrencyService
{
    Task<ExchangeRatesResponse> GetRatesAsync(string baseCurrency);

    decimal Convert(
        decimal amount,
        decimal fromRate,
        decimal toRate
    );
}