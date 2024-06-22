package main
import (
    "github.com/gin-gonic/gin"
    "github.com/prometheus/client_golang/api"
    v1 "github.com/prometheus/client_golang/api/prometheus/v1"
)
func main() {
    // Подключение к Prometheus API
    client, err := api.NewClient(api.Config{
        Address: "http://prometheus:9090",
    })
    if err != nil {
        panic(err)
    }
    apiV1 := v1.NewAPI(client)
    r := gin.Default()
    r.GET("/metrics", func(c *gin.Context) {
        // Получение метрик Nginx-серверов
        result, _, err := apiV1.Query(c, `sum(rate(nginx_connections_active{job="nginx"}[1m])) by (instance)`)
        if err != nil {
            c.JSON(500, gin.H{"error": err.Error()})
            return
        }

        // Предобработка данных
        metrics := processMetrics(result)
        c.JSON(200, metrics)
    })
    r.Run()
}
func processMetrics(result v1.Result) []map[string]interface{} {
    // Заполнение пропусков, сглаживание, нормализация данных
    // ...
    return metrics
}
