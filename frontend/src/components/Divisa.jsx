import React, { useEffect, useState } from "react";
import { Card, useColorModeValue } from '@chakra-ui/react'
import { GridItem } from '@chakra-ui/react'
import {
    Stat,
    StatLabel,
    StatNumber,
    StatHelpText,
    StatArrow,
    StatGroup,
} from '@chakra-ui/react'


export default function Divisa(props) {

    return (
        <GridItem>
            <Card
                direction={{ base: 'column', sm: 'row' }}
                overflow='hidden'
                variant='outline'
                color="gray"
                px="2"
                pt="3"
                bg={useColorModeValue('blue', 'black')}                
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
                                <StatHelpText>
                                    <StatArrow type="increase" />
                                    23.36%
                                </StatHelpText>
                            </Stat>
                        </GridItem>
                        <GridItem pl="2">
                            <Stat>
                                <StatLabel>Venta</StatLabel>
                                <StatNumber>{divisa.venta} PYG</StatNumber>
                                <StatHelpText>
                                    <StatArrow type="decrease" />
                                    9.05%
                                </StatHelpText>
                            </Stat>
                        </GridItem>
                    </Grid>
                </StatGroup>
            </Card>
        </GridItem>

    )
}