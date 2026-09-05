---
type: note
domain: finances
created: 2026-09-05
updated: 2026-09-05
lang: pt
links:
  - "https://docs.google.com/spreadsheets/d/15qSiPTHYmzh1_ItzET0VZStiVu32KEodbBxU30Sl78w/"
  - "https://docs.google.com/spreadsheets/d/13cod5YUveCILRhjTISBC6xe8za1xNRLSjFkRw4edFxg"
---

# Cash burn — como medir

O valor vive na planilha de fluxo de caixa. Esta nota fixa **como derivá-lo**, porque o total de `Débito` da planilha **não é** o burn.

## O erro de ler o Débito direto

A planilha lança transferências de poupança como `Débito`:

- `Reembolso Reserva de emergência` — aporte na reserva
- `Reembolso Provisão cartões de crédito` — aporte no fundo que cobre a dívida de cartão

As duas **constroem patrimônio**. Somá-las ao burn faz um mês de poupança alta parecer um mês de gasto alto — e foi exatamente o que aconteceu nas leituras anteriores do vault.

## Método

```
burn = Débito total − Reembolso Reserva de emergência − Reembolso Provisão cartões de crédito
```

Ler na planilha [2026 - Planejamento de Gastos](https://docs.google.com/spreadsheets/d/15qSiPTHYmzh1_ItzET0VZStiVu32KEodbBxU30Sl78w/) via Drive MCP. As abas são `Jan`…`Dez` (nomes curtos — `Janeiro!` não resolve). Totais em `C3:C8`; entradas em `C10:F…`; saídas em `K10:M…`.

## Qual mês usar como referência

Use um **mês de salário puro** — só a entrada `Salário | Yandeh`, sem equity Fluencypass, sem 13º, sem rescisão. Meses com renda extraordinária inflam tanto o aporte na reserva quanto as despesas eventuais, e não representam o regime permanente.

A partir de **nov/2026** todos os meses são assim: a última parcela de equity da Fluencypass cai em out/2026 e o contrato de horas se encerra. Renda passa a ser **fonte única** — um contrato PJ, sem FGTS e sem seguro-desemprego. Isso é o que justifica a reserva, não o conforto.

Ao ler, separe também os **gastos sazonais** do mês (aniversários, presentes de fim de ano, IPVA) para não confundir pico com base.

## O que a leitura de 2026-09-05 mostrou

- O burn recorrente está **~60% acima** da premissa de R$ 17.320,70 usada no replanejamento de mai/2026 — premissa que atravessa [[raw/Plans/Relocation|o plano de relocação]]. Todos os prazos derivados dela estão errados.
- Quase todo o aumento é **provisão discricionária nova** (Saldo Livre por pessoa, provisão Iood, alimentação, suplementos), não custo fixo. É a alavanca mais barata que existe: cortar burn move ao mesmo tempo o quanto sobra por mês **e** o tamanho da meta de reserva.
- A taxa de poupança real de ago–dez/2026 passa de metade das entradas. O saldo mensal perto de zero na planilha não é aperto — é alocação.

## Metas ancoradas no burn

Os alvos são múltiplos do **burn cheio replanejado**, não do essencial — o padrão de vida discricionário faz parte da meta:

| Alvo | Definição |
|---|---|
| Reserva curto prazo | 1 × burn |
| Reserva médio prazo | 6 × burn |
| Reserva longo prazo | 12 × burn |
| Renda passiva / independência | burn cheio coberto por proventos |

Como os alvos são derivados, **eles se movem quando o burn se move**. Recalcular a cada revisão, nunca reusar um número escrito antes.

## Achados em aberto (verificar na planilha)

1. **ISS-Equity em nov/2026** — a linha `Yago Silva Sistemas (ISS) - Equity` aparece em novembro, mas não há entrada de equity nesse mês. Em ago/set/out o imposto é lançado no mesmo mês da receita, e dez corretamente não tem. Provável linha residual.
2. **Convênio** — out lança valor; set, nov e dez lançam zero. O plano SulAmérica da Yandeh não tem mensalidade ([[raw/Career/Yandeh/Details|Details]]); ou é coparticipação e falta nos outros meses, ou sobra em outubro.
3. **Parcela do cartão fora do fluxo** — `Cartão Rico` e `Cartão Nubank` estão zerados em todos os meses; a parcela consome a provisão, não o salário. Logo, o fim do parcelamento **não libera fluxo mensal** — libera a provisão. A premissa contrária em [[raw/Plans/Relocation|Relocation]] está incorreta.
4. **Veículos** — carro e moto somam uma fatia relevante da renda bruta em custeio recorrente, e o capital parado neles é grande frente ao que existe de líquido. A moto **está registrada** desde 2026-09-05 como o transporte do Yago para o trabalho ([[raw/Finances/Overview|Overview]] → `Vehicles`), logo o custeio dela é deslocamento, não discricionário. A pergunta em aberto passou a ser qual dos **dois** veículos a família precisa.
