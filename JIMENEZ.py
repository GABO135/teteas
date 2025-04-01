import React, { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

const CombustionBalancer = () => {
  const [formula, setFormula] = useState("");
  const [result, setResult] = useState("");

  const balanceCombustion = (formula) => {
    const match = formula.match(/^C(\d*)H(\d*)$/);
    if (!match) return "Formato incorrecto. Usa CxHy.";
    
    const x = match[1] ? parseInt(match[1]) : 1;
    const y = match[2] ? parseInt(match[2]) : 1;
    
    const co2 = x;
    const h2o = Math.floor(y / 2);
    const o2 = (2 * co2 + h2o) / 2;
    
    if (!Number.isInteger(o2)) {
      return "No es posible balancear con números enteros.";
    }
    
    return `${formula} + ${o2} O₂ → ${co2} CO₂ + ${h2o} H₂O`;
  };

  return (
    <div className="p-4 max-w-lg mx-auto">
      <Card>
        <CardContent className="p-4 space-y-4">
          <h2 className="text-xl font-bold">Balanceador de Combustión</h2>
          <Input
            placeholder="Ingresa la fórmula (ej. C2H6)"
            value={formula}
            onChange={(e) => setFormula(e.target.value)}
          />
          <Button onClick={() => setResult(balanceCombustion(formula))}>
            Balancear
          </Button>
          {result && <p className="text-lg font-semibold">{result}</p>}
        </CardContent>
      </Card>
    </div>
  );
};

export default CombustionBalancer;
