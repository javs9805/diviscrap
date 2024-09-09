import React, { useEffect, useState } from "react";
import { Card, CardHeader, CardBody, CardFooter, useColorMode, useColorModeValue } from '@chakra-ui/react'
import { Heading } from '@chakra-ui/react'
import { Grid, GridItem } from '@chakra-ui/react'
import { Container } from '@chakra-ui/react'
import {
  Stat,
  StatLabel,
  StatNumber,
  StatHelpText,
  StatArrow,
  StatGroup,
} from '@chakra-ui/react'
import { Divider } from '@chakra-ui/react'


const DivisasContext = React.createContext({
  divisas: [], 
  fetchDivisas: () => { }
})

export default function Divisa(props) {

  const bgColor = useColorModeValue('gray.200', 'black.200')
  const fontColor = useColorModeValue('black', 'white')

  const [divisas, setDivisas] = useState([])
  const [nombreCasaCambio, setnombreCasaCambio] = useState([])
  const fetchDivisas = async () => {
    const endpoint = props.casa;
    const response = await fetch(`http://localhost:8000/casa/${endpoint}/`)
    const divisas = await response.json()
    console.table(divisas);
    setDivisas(divisas.currency)
    setnombreCasaCambio(divisas.name)
  }
  useEffect(() => {
    fetchDivisas()
  }, [])


  return (
    <DivisasContext.Provider value={{ divisas, fetchDivisas }}>
      <Container
        color='#262626'
        maxW='4xl'
        pt="1rem"
      >
        <Heading color={fontColor}>{nombreCasaCambio}</Heading>
        <Divider w={3} pb={2}/>
        <Grid templateColumns='repeat(2, 1fr)' gap={6}>
          {divisas.map((divisa) => (
            <GridItem>
              <Card
                direction={{ base: 'column', sm: 'row' }}
                overflow='hidden'
                px="2"
                pt="3"
                bg={bgColor}
              >
                <StatGroup w="90%">
                  <Grid
                    templateAreas={`"header header"
                      "nav main"
                    "nav main"`}
                    gap="1"
                    w="100%"
                  >
                    <GridItem pl="2" area={"header"}>
                      {divisa.nombre}
                    </GridItem>
                    <GridItem pl="2">
                      <Stat>
                        <StatLabel>Compra</StatLabel>
                        <StatNumber>{divisa.compra} PYG</StatNumber>
                        {/*
                        <StatHelpText>
                          <StatArrow type="increase" />
                          23.36%
                        </StatHelpText>
                        */}
                      </Stat>
                    </GridItem>
                    <GridItem pl="2">
                      <Stat>
                        <StatLabel>Venta</StatLabel>
                        <StatNumber>{divisa.venta} PYG</StatNumber>
                        {/*
                        <StatHelpText>
                          <StatArrow type="decrease" />
                          9.05%
                        </StatHelpText>
                        */}
                      </Stat>
                    </GridItem>
                  </Grid>
                </StatGroup>
              </Card>
            </GridItem>
          ))}
        </Grid>
      </Container>
    </DivisasContext.Provider>
  )
}